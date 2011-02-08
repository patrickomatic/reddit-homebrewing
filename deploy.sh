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


if [ "$1" = "--help" -o "$1" = "-h" ]; then
	usage 0
elif [ "X$1" != "X" ]; then
	usage 1
else
	for INST in `sed -e 's/#.*$//' $INSTANCES_FILE`; do sync_code $INST; done
fi

