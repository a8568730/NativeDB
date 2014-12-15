/* 首頁 */

var app = angular.module("app1",['ngRoute']);

app.controller("LangController",["$scope", "$log","$http", function($scope, $log, $http){
	$scope.langs = [];
	$http({
			method: 'GET',
			url: '/語言表全部json',
			data: {}
	}).success(function(data, status) {
			$scope.langs = data;
			console.log(status);
	});
	$scope.call = function(lang){
		$log.log(lang);
	};
}]);
