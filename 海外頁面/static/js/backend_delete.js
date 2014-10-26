var app1 = angular.module('app1',['ngRoute']);

app1.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app1.controller('DeleteController', ['$scope','FileService', function($scope, FileService){
	var corpus = 2;
	//得到檔案編號與檔名的list
	$scope.files = FileService.GetFileList(corpus);
}]);

/*$scope不是service, 是Scope物件。不可放$scope在service*/
app1.service('FileService', function($http, $log){
	this.GetFileList = function(corpus){
		var list=[];
		console.log(corpus);
		$http({
			method: 'GET',
			url: '/語料的全部檔案json',
			data: {},
			params: {pk: 2}
		})
		.success(function(data, status){
			angular.forEach(data, function(line, key) {
				  list.push(line);
			});
			console.log('files:'+ list);
		});
		return list;	
	};
	this.DeleteFile = function(){
		//delete the file
		
		//get new list
	};
});
