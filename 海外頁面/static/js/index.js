var app = angular.module("app1",['ui.bootstrap', 'ngRoute']);

/* 主頁 */
//Method 1:  directive
app.directive('languageFlag', function() {
	return function($scope, element, attrs) {
		//		observe data-sui2
	    attrs.$observe('sui2', function(value) {
	        $scope.sui2sui2 = value;
	    });
	}
});
app.controller("indexController",["$scope", "$log","$http","$routeParams", "$route", "$location","$window",
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
					isactive = (data[i] == $scope.sui2sui2) ? true : false;
					$scope.tabs.push({"lang":data[i], "active": isactive});
					console.log({"lang":data[i], "active": isactive});
				};
				console.log($scope.tabs);
				console.log('sui2=' + $scope.sui2sui2);
		});
		
		//	切換其他分頁時，改網址
		$scope.refresh = function(somelang){
			if(somelang !=  $scope.sui2sui2){
				//	$window.location.href = '/index/' + somelang;
				//$location.path('/index/' + somelang);
				$location.path(somelang);
				$scope.sui2sui2 = somelang;
			}
		};
}]);

////Method 2:	$routeParams
////1. inject $route and $routeParams to get url params
//app.config(function($routeProvider, $locationProvider) {
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