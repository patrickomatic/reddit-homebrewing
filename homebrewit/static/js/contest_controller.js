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
        angular.forEach($scope.styleChosen.beer_details, function(question) {
            question.value = '';
        });
    };


    $scope.registerForContest = function() {
        $http.post('/contests/' + $scope.contestYear + '/beer_styles/' + $scope.styleChosen.id, $scope.styleChosen).success(function(data) {
            console.log("did it success");
        }).error(function(data) {
            console.log("it failed");   
        });
    };
});
