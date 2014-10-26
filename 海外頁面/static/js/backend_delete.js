var app1 = angular.module('app1',['ngRoute']);

//app1.directive('deleteFile', function(){
//	
//});

app1.controller('DeleteController', ['$scope', '$http', '$log', function($scope, $http, $log){
	$scope.info = 2;
	//得到檔案編號與檔名的list
	$http({
		method: 'GET',
		url: '/語料的全部檔案json',
		data: {},
		params: {pk:$scope.info}
	}).success(function(data, status) {
		$scope.files = data;
		console.log('files:'+$scope.files);
	});
	//
}]);


app1.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});