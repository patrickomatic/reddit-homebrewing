var contestApp = angular.module('contestApp', []);

contestApp.controller('ContestSignupCtrl', function($scope, $http) {
	$http.get('/contests/2013/beer_styles').success(function(data) {
		$scope.styles = data;
	});
});

