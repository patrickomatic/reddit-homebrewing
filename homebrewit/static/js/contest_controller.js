var contestApp = angular.module('contestApp', []);

contestApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'; 
}]);

contestApp.directive("ngConfirmClick", [
    function() {
        return {
            link: function(scope, element, attr) {
                element.bind('click', function(event) {
                    if (window.confirm(attr.ngConfirmClick || "Are you sure?"))
                        scope.$eval(attr.ngConfirmedClick);
                });
            }
        };
    }
]);

contestApp.controller('ContestSignupCtrl', function($scope, $http, $location) {
    $scope.init = function(contestYear) {
        if (contestYear) { 
            $scope.contestYear = contestYear;

            $http.get('/contests/' + $scope.contestYear + '/beer_styles').success(function(data) {
                $scope.styles = data;
                $scope.entry = {};
            });
        }
    };

    $scope.chosen = function(style) {
        $scope.entry.style = style;
    };


    $scope.deleteEntry = function(id, styleId, contestYear) {
        $http.delete('/contests/' + contestYear + '/styles/' + styleId + '/entries/' + id).success(function(data) { 
            // XXX better experience here, no need to reload
            window.location = "/profile/";
        });
    };

    $scope.registerForContest = function() {
        $scope.submitting = true;
        var entry = $scope.entry;

        $http.post('/contests/' + $scope.contestYear + '/styles/' + $scope.entry.style.id + '/entries', {
            style: entry['style']['id'],
            beer_name: entry['beer_name'],
            special_ingredients: entry['special_ingredients'],
            entry_beer_details: entry['style']['beer_details'].map(function(e) { return {beer_detail: e.id, value: e.value}; })
        }).success(function(data) {
            // XXX set an alert 
            window.location = "/profile/";
        }).error(function(data) {
            // XXX do something better
            alert("There was an error regsitering, please contact the moderators if this persists");
        });
    };
});
