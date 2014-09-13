// Code goes here

var app = angular.module("app1",['ui.bootstrap']);

app.controller("LangController",["$scope", "$log","$http", function($scope, $log, $http){
	$scope.langs = [];
	$http({
			method: 'GET',
			url: '/語言表全部json',
			data: {}
	}).success(function(data, status) {
			$scope.langs = data;
	});

	$scope.call = function(lang){
		$log.log(lang);
	};
}]);


/* 解決 Django 和 AngularJS共用{{}}的混淆問題 */
app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});