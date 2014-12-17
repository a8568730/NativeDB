var app = angular.module("app1",['ui.bootstrap', 'ngRoute']);

/* 主頁 */
//取得網址的語言參數方法:  directive
app.directive('getUrlLang', function() {
	return function($scope, element, attrs) {
		//	取得 data-lang 的值為此網頁初次查看的語言
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
					isactive = false;
					if(data[i] == $scope.lang){
						// 第一次讀資料
						getCorpusData(data[i], i);
						isactive = true;
					}
					$scope.tabs.push({"lang":data[i], "active": isactive, "contents":[]});
					console.log({"lang":data[i], "active": isactive});
				};
				console.log($scope.tabs);
				console.log('current lang=' + $scope.lang);
		});
		
		//	切換其他分頁時，改網址，並讀資料
		$scope.refresh = function(lang, tabindex){
			if(lang !=  $scope.lang){
				//	$window.location.href = '/index/' + somelang; //$location.path('/index/' + somelang);
				// 改網址
				$location.path(lang);
				$scope.lang = lang;
				// 讀資料
				getCorpusData(lang, tabindex);
			}
		};
		
		var getCorpusData = function(lang, tabindex){
			// 讀一語言的資料
			//	輸出格式 {	
			//			MoT: [ [{word:字, IPA:音標, wavs:[音檔, 音檔]}] , 音檔數量] }
			$http({
				method: 'GET',
				url: '/' + lang + '/顯示語言漢字相同的音檔',
				data: {}
			}).success(function(data, status){
				$scope.tabs[tabindex].types = data;
				console.log(data);
			});
		};
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