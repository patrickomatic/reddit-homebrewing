var contestApp = angular.module('contestApp', []);

contestApp.controller('ContestSignupCtrl', function($scope, $http) {
	$scope.styles = [
		{'name': 'IPA', 'value': '1'},
		{'name': 'Stout', 'value': '2'}
	];
	$scope.beerStyle = 'IPA';
});

