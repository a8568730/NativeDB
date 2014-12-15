var app = angular.module("app1",['ui.bootstrap', 'ngRoute']);

/* 主頁 */
//取得網址參數方法:  directive
app.directive('getUrlLang', function() {
	return function($scope, element, attrs) {
		//	取得 data-lang 的值
	    attrs.$observe('lang', function(value) {
	        $scope.lang = value;
	    });
	}
});
app.controller("indexController",["$scope", "$log", "$http", "$routeParams", "$route", "$location", "$window",
	function($scope, $log, $http,$routeParams, $route, $location, $window){
		$scope.tabs = [];
		$http({
				method: 'GET',
				url: '/語言表全部json',
				data: {}
		}).success(function(data, status) {
				// 取得網址的語言參數後，此語言的頁面顯示為true
				var isactive;
				for(var i=0; i<data.length; i++){
					isactive = (data[i] == $scope.lang) ? true : false;
					$scope.tabs.push({"lang":data[i], "active": isactive});
					console.log({"lang":data[i], "active": isactive});
				};
				console.log($scope.tabs);
				console.log('current lang=' + $scope.lang);
		});
		
		//	切換其他分頁時，改網址，並讀資料
		$scope.refresh = function(somelang){
			if(somelang !=  $scope.lang){
				//	$window.location.href = '/index/' + somelang; //$location.path('/index/' + somelang);
				$location.path(somelang);
				$scope.lang = somelang;
				$http({
					method: 'GET',
					url: somelang + '/顯示語言漢字相同的音檔',
					data: {}
				}).success(function(data, status){
					console.log(data);
				});
			}
		};
		// 讀入此語料的
}]);

////取得網址參數方法 2:	$routeParams
////1. inject $route and $routeParams to get url params
////app.config(function($routeProvider, $locationProvider) {
//	  $routeProvider
//	  	.when('/index/', {redirectTo: '/index/豬豬語'})
//	  	.when('/index/:language', {
//	    controller: 'indexController'
//	  });
//	  $locationProvider.html5Mode(true);
//});
////2. inject $route and $routeParams to get url params  
////index/媠媠媠
//app.controller("indexController",["$scope", "$log","$http","$routeParams", "$route", "$location","$window",
//	function($scope, $log, $http,$routeParams, $route, $location, $window){
//		$scope.param = $routeParams;
//		console.log($scope.param);
//}]);