// Code goes here

var app = angular.module("app1",['ui.bootstrap','ngRoute']);

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

app.controller("indexController",["$scope", "$log","$http","$routeParams", "$route", 
	function($scope, $log, $http,$routeParams, $route){
		$scope.langs = [];
		
		$http({
				method: 'GET',
				url: '/語言表全部json',
				data: {}
		}).success(function(data, status) {
				$scope.langs = data;
		});
		//	inject $route and $routeParams to get url params 
		$scope.param = $routeParams;
		console.log($scope.param);
}]);

app.config(function($routeProvider, $locationProvider) {
	  $routeProvider
	   .when('/index/:language', {
	    controller: 'indexController'
	  });

	  // configure html5 to get links working on jsfiddle
	  $locationProvider.html5Mode(true);
	});

/* 解決 Django 和 AngularJS共用{{}}的混淆問題 */
app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});