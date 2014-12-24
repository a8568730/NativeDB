var app = angular.module("app1",['ui.bootstrap', 'ngRoute']);

/* 主頁 */
//取得網址的語言參數方法:  directive
app.directive('getUrlParams', function() {
	return function($scope, element, attrs) {
		//	取得 data-lang 的值為此網頁初次查看的語言
	    attrs.$observe('lang', function(value) {
	        $scope.lang = value;
	    });
	    attrs.$observe('hanji', function(value) {
	    	$scope.Hanji = value;
	    });
	    attrs.$observe('ipa', function(value) {
	    	$scope.IPA = value;
	    });
	};
});
app.controller("detailController",["$scope", "$log", "$http", "$routeParams", "$route", "$location", "$window",
	function($scope, $log, $http,$routeParams, $route, $location, $window){
		$scope.tabs = [];
		$scope.contents ={};
		// 取得導覽列的語言
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
						isactive = true;
						// 取得同一字但是不同的語料和音檔
						getHanjiFiles(data[i], i);
					}
					$scope.tabs.push({"lang":data[i], "active": isactive, "contents":[]});
				};
		});
		
		var getHanjiFiles = function(){
			$http({
				method: 'GET',
				url: '/' + $scope.lang + '/' + $scope.Hanji +  '/' + $scope.IPA + '/輸出同語言一漢字的所有音檔',
				data: {}
			})
			.success(function(data, status) {
				// 輸出格式 {	
					//		word:字, 
					//		IPA:音標, 
					//		wavs: [{locate: 所在, age: 年歲, sex: 性別, wav: 音檔}, {locate: 所在, age: 年歲, sex: 性別, wav: 音檔}], 
					// 	}
				console.log(data);
				$scope.infos=data;  
			});
		};
		
		//播放<audio>標籤的音樂
		$scope.clicked = false;
		$scope.play = function(id){
            var activeSong = document.getElementById(id);
            if (activeSong.paused){
            	$scope.clicked = true;
            	activeSong.play();
            }else{
            	$scope.clicked = false;
            	activeSong.pause();
            } 
            activeSong.addEventListener('ended', function(){
            	$scope.$apply( function() {
            		$scope.clicked = false;
                });
            });
        };
        
		//	切換其他分頁時，改網址，並讀資料
		$scope.redirectTo = function(lang, tabindex){
			//$window.location.href = '/index/' + lang; 
			//$location.path('/index/' + lang);
			if(lang!=$scope.lang){
				$window.location.href = '/index/' + lang;
			}
//				// 改網址
//				$location.path(lang);
//				$scope.lang = lang;
//				// 讀資料
//				//getCorpusData(lang, tabindex);
//			}
		};
}]);