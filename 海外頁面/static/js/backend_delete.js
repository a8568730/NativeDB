var app1 = angular.module('app1',['ngRoute']);

app1.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app1.directive('getCorpus', function() {
	return function($scope, element, attrs) {
		//		observe data-corpus
	    attrs.$observe('corpus', function(value) {
	    	console.log('$scope.corpus=' + value);
	        $scope.corpus = value;
	    });
	}
});

app1.controller('DeleteController', ['$scope','FileService', function($scope, FileService){
	//抓網址取出語料編號
	$scope.GetFiles = function(corpus){ $scope.files = FileService.GetFileList(corpus); };
	$scope.RemoveFiles = function(ID){ FileService.DeleteFile(ID, $scope.files);};

	// 初始網頁，得到檔案編號與檔名的list
	console.log('$scope.corpus=' + $scope.corpus);
	$scope.GetFiles($scope.corpus);
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
