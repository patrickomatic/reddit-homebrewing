var contestApp = angular.module('contestApp', []);

contestApp.controller('ContestSignupCtrl', function($scope, $http) {
    $scope.init = function(contestYear) {
        $scope.contestYear = contestYear;

        $http.get('/contests/' + $scope.contestYear + '/beer_styles').success(function(data) {
            $scope.styles = data;
            $scope.style = data[0];
            console.log($scope.styles); // XXX
        });
    };

    $scope.chosen = function(style) {
        $scope.styleChoice = style;
    };


    $scope.registerForContest = function() {
        $http.post('/contests/' + $scope.contestYear + '/beer_styles/' + $scope.styleChosen.id, $scope.styleChosen).success(function(data) {
            console.log("did it success");
        }).error(function(data) {
            consooe.log("it failed");   
        });
    };
});
