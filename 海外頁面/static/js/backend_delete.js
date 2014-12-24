var app1 = angular.module('app1',['ngRoute']);

app1.controller('DeleteController', ['$scope','FileService', '$route', '$routeParams', '$location', 
                                     function($scope, FileService, $route, $routeParams, $location){
	//在HTML呼叫的服務
	$scope.GetFiles = function(corpus){ $scope.files = FileService.GetFileList(corpus); };
	$scope.RemoveFiles = function(ID){ console.log('file[0]=' + ID); FileService.DeleteFile(ID, $scope.files); };

	//取得網址參數的語料編號
	$scope.$route = $route;
    $scope.$location = $location;
    $scope.$routeParams = $routeParams;
    
	//請求此語料的所有檔案名稱清單
   $scope.showfiles = false;
	$scope.go = function(){
		console.log('go, $scope.corpus=' + $routeParams['corpus']);
		$scope.showfiles = true;
		$scope.GetFiles($routeParams['corpus']);
	};
}]);

app1.config(['$routeProvider', '$locationProvider', '$interpolateProvider', 
		function($routeProvider, $locationProvider, $interpolateProvider) {
			$locationProvider.html5Mode(true);
			//http://127.0.0.1:8000/3/揣著語料的全部檔案
			$routeProvider
    		.when('/:corpus/揣著語料的全部檔案', {
				templateUrl: '../../templates/海外頁面/顯示全部檔案.html',  
				controller: 'DeleteController'
    		});
			
		$interpolateProvider.startSymbol('{$');
		$interpolateProvider.endSymbol('$}');	
}]);

app1.service('FileService', function($http, $log){
	// 筆記：$scope不是service, 是Scope物件。不可放$scope在service
	this.GetFileList = function(corpus){
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
	
	this.DeleteFile = function(ID, files){
		//1. delete the file
		$http({
			method: 'GET',
			url: '/'+ ID + '/刪除一個檔案',
			data: {},
		}).success(function(){
			//2. remove the item from file list
			for(var i=0; i < files.length; i++){
				if(ID == files[i][0]){
					files.splice(i, 1);
					break;
				}	
			}
			console.log('delete done!');
		}).error(function(){
			console.log('failed to delete');
		});	
	};
	
});
