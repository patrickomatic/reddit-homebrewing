#!/bin/sh

LAUNCH_DIR=`dirname $0`
INSTANCES_FILE=$LAUNCH_DIR/INSTANCES
DEPLOY_DIR=/srv/homebrewit
ADMIN_PATH=/usr/lib/python2.5/site-packages/django/contrib/admin/media/


usage() {
	echo "Usage: $0 [install HOST_NAME]" >&2
	exit $1
}

sync_code() {
	git checkout master
	rsync -avz --rsh=ssh --delete --exclude "*.swp" --exclude "*.pyc" \
			$LAUNCH_DIR/homebrewit $LAUNCH_DIR/media  $LAUNCH_DIR/templates \
			$LAUNCH_DIR/apache root@$1:$DEPLOY_DIR
	ssh root@$1 "ln -s $ADMIN_PATH $DEPLOY_DIR/media/admin; /etc/init.d/apache2 restart"
	ssh root@$1 "chown -R django:django $DEPLOY_DIR"
}

install() {
	HOST=$1
	ssh root@$HOST "id django >/dev/null 2>&1 || useradd django"
	ssh root@$HOST "[ -d $DEPLOY_DIR/logs ] || mkdir -p $DEPLOY_DIR/logs"

	ssh root@$HOST "rm -f /etc/apache2/sites-enabled/* /etc/apache2/sites-available/*"
	ssh root@$HOST "cat > /etc/apache2/sites-available/homebrewit" <<__EOF
<VirtualHost *:80>
    ServerAdmin patrick@patrickomatic.com
    ServerName $HOST

    Alias /media/ ${DEPLOY_DIR}/media/
    Alias /robots.txt ${DEPLOY_DIR}/media/robots.txt 
    Alias /favicon.ico ${DEPLOY_DIR}/media/favicon.ico 

    CustomLog "|/usr/sbin/rotatelogs ${DEPLOY_DIR}/logs/access.log.%Y%m%d-%H%M%S 5M" combined
	ErrorLog "|/usr/sbin/rotatelogs ${DEPLOY_DIR}/logs/error.log.%Y%m%d-%H%M%S 5M"
    LogLevel warn

    WSGIDaemonProcess slackjaw.dyercpa.com user=django group=django processes=1 threads=15 maximum-requests=10000 
    WSGIProcessGroup slackjaw.dyercpa.com
    WSGIScriptAlias / ${DEPLOY_DIR}/apache/django.wsgi

    <Directory ${DEPLOY_DIR}/media>
        Order deny,allow
        Allow from all
        Options -Indexes FollowSymLinks
    </Directory>

    <Directory ${DEPLOY_DIR}/apache>
        Order deny,allow
        Allow from all
    </Directory>
</VirtualHost>
__EOF
	ssh root@$HOST "ln -s /etc/apache2/sites-available/homebrewit /etc/apache2/sites-enabled/homebrewit"

	sync_code $HOST

	exit 0	
}


if [ "$1" = "--help" -o "$1" = "-h" ]; then
	usage 0
elif [ "$1" = "install" ]; then
	if [ "X$2" = "X" ]; then
		usage 1
	else
		install $2
	fi
elif [ "X$1" != "X" ]; then
	usage 1
else
	for INST in `sed -e 's/#.*$//' $INSTANCES_FILE`; do sync_code $INST; done
fi

