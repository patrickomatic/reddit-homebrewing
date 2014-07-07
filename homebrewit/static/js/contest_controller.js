var contestApp = angular.module('contestApp', []);

contestApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'; 
}]);

contestApp.controller('ContestSignupCtrl', function($scope, $http) {
    $scope.init = function(contestYear) {
        $scope.contestYear = contestYear;

        $http.get('/contests/' + $scope.contestYear + '/beer_styles').success(function(data) {
            $scope.styles = data;
            $scope.entry = {};
        });
    };

    $scope.chosen = function(style) {
        $scope.entry.style = style;
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
            console.log("did it success");
        }).error(function(data) {
            console.log("it failed");
        });
    };
});
