/* 解決 Django 和 AngularJS共用{{}}的混淆問題 */
app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});