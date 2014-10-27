

var app = angular.module('app1',['ngRoute']);

app.controller('UrlController', ['$scope', '$http', '$route', '$routeParams', '$log', '$location', 
                                 function($scope, $http, $route, $routeParams, $log, $location){
	var GetFileList = function(corpus){
		var list=[];
		console.log('GetFileList, corpus=' + corpus);
		$http({
			method: 'GET',
			url: '/語料的全部檔案json',
			data: {},
			params: {pk: corpus}
		})
		.success(function(data, status){
			angular.forEach(data, function(line, key) {
				  list.push(line);
			});
			console.log('files:'+ list);
		});
		return list;
		
	};
	
	//取得網址參數的語料編號
	$scope.$route = $route;
    $scope.$location = $location;
    $scope.$routeParams = $routeParams;
    
	$scope.corpus = $routeParams.corpus;
	//請求檔案
	$scope.go = function(){
		console.log('go, $scope.corpus=' + $routeParams['corpus']);
		$scope.files = GetFileList($routeParams.corpus);
	};
	
}]);


app.config(['$routeProvider', '$locationProvider', '$interpolateProvider', 
		function($routeProvider, $locationProvider, $interpolateProvider) {
	$locationProvider.html5Mode(true);
	$routeProvider
		.when('/測試抓網址/:corpus', {
			templateUrl: '../../templates/海外頁面/測試抓網址.html',  
			controller: 'UrlController'
	});
	
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
}]);