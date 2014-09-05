// Code goes here

var app = angular.module("app1",[]);

app.controller("LangController",["$scope", "$log", function($scope, $log){
  $scope.langs = ["華語", "閩語", "客語"];
  $scope.call = function(lang){
	  $log.log(lang);
  };
}]);

/* 解決 Django 和 AngularJS共用{{}}的混淆問題 */
app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});