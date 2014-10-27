// Code goes here

var app = angular.module("app1",['ui.bootstrap','ngRoute']);

app.directive('languageFlag', function() {
	return function($scope, element, attrs) {
		//		observe data-sui2
	    attrs.$observe('sui2', function(value) {
	        $scope.sui2sui2 = value;
	    });
	}
});

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

app.controller("indexController",["$scope", "$log","$http","$routeParams", "$route", "$location","$window",
	function($scope, $log, $http,$routeParams, $route, $location, $window){
		//		Method 1 :
		//			inject $route and $routeParams to get url params
		// 			index/媠媠媠
		//			$scope.param = $routeParams;
		//			isactive = (data[i] == $scope.param.language) ? true : false;
	
		//		Method 2 :	directive
		$scope.tabs = [];
		$http({
				method: 'GET',
				url: '/語言表全部json',
				data: {}
		}).success(function(data, status) {
				var isactive;
				for(var i=0; i<data.length; i++){
					isactive = (data[i] == $scope.sui2sui2) ? true : false;
					$scope.tabs.push({"lang":data[i], "active": isactive});
					console.log({"lang":data[i], "active": isactive});
				};
				console.log($scope.tabs);
				console.log('sui2=' + $scope.sui2sui2);
		});
		
		$scope.refresh = function(somelang){
			//		改網址
			if(somelang !=  $scope.sui2sui2){
//					$window.location.href = '/index/' + somelang;
				$location.path('/index/' + somelang);
				$scope.sui2sui2 = somelang;
			}
//			if(!$scope.$$phase) $scope.$apply();
		};
}]);


//		Method 1 :
//			inject $route and $routeParams to get url params
//app.config(function($routeProvider, $locationProvider) {
//	  $routeProvider
//	  	.when('/index/', {redirectTo: '/index/豬豬語'})
//	  	.when('/index/:language', {
//	    controller: 'indexController'
//	  });
//	  $locationProvider.html5Mode(true);
//});

/* 解決 Django 和 AngularJS共用{{}}的混淆問題 */
app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});