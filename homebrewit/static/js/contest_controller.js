var contestApp = angular.module('contestApp', []);

contestApp.controller('ContestSignupCtrl', function($scope, $http) {
    $scope.init = function(contestYear) {
        $scope.contestYear = contestYear;
    };

    $scope.status = {
        isopen: false
    };

    $scope.toggled = function(open) {
        console.log("it is ", open);
    };

    $scope.toggleDropdown = function($event) {
        $event.preventDefault();
        $event.stopPropagation();
        $scope.status.isopen = !$scope.status.isopen;
    }

	$http.get('/contests/2011/beer_styles').success(function(data) {
		$scope.styles = data;
		$scope.style = data[0];
	});

    $scope.registerForContest = function($http) {
        $http.post('/contests/' + $scope.contestYear + '/beer_styles/' + $scope.style);
    };
});
