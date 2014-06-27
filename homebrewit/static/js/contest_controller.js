var contestApp = angular.module('contestApp', []);

contestApp.controller('ContestSignupCtrl', function($scope, $http) {
    $scope.init = function(contestYear) {
        $scope.contestYear = contestYear;

        $http.get('/contests/' + $scope.contestYear + '/beer_styles').success(function(data) {
            $scope.styles = data;
            $scope.style = data[0];
        });
    };

    $scope.chosen = function(style) {
        $scope.styleChosen = style;
    };


    $scope.registerForContest = function() {
        $scope.submitting = true;

        // XXX get this working and we're done!
        $http.post('/contests/' + $scope.contestYear + '/beer_styles/' + $scope.styleChosen.id, $scope.styleChosen).success(function(data) {
            console.log("did it success");
        }).error(function(data) {
            console.log("it failed");   
        });
    };
});
