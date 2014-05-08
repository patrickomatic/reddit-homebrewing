var contestApp = angular.module('contestApp', []);

contestApp.controller('ContestSignupCtrl', function($scope, $http) {
    $scope.init = function(contestYear) {
        $scope.contestYear = contestYear;
    };

    console.log($scope.contestYear);

	$http.get('/contests/2011/beer_styles').success(function(data) {
		$scope.styles = data;
		$scope.style = data[0];
	});

    $scope.registerForContest = function($http) {
        $http.post('/contests/' + $scope.contestYear + '/beer_styles/' + $scope.style);
    };
});
