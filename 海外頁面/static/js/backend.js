angular.module('app1',[])
		.controller('BackendController', ['$scope', function($scope){
			$scope.panels = [
	                 {
	                	 head: '語言',
	                	 links: [{path:'加語言表表格', text:'新增語言'}]
	                 },{
	                	 head: '類型',
	                	 links: [{path:'加類型表表格', text:'新增類型'}]
	                 },{
	                	 head: '語料',
//	                	 links: [{path:'加原始語料表表格', text:'新增語料(地區，年齡，性別，ID)'},
//	                	         {path:'顯示原始語料表', text:'顯示所有原始語料'}]
	                	 links: [{path:'加原始語料表表格', text:'新增語料(地區，年齡，性別，ID)'}]
	                 }
//	                 ,{
//	                	 head: '檔案',
//	                	 links: [{path:'上傳檔案', text:'上傳檔案'}]
//	                 }
		];
}])

//<li><a href="{% url '加語言表表格' %}">新增語言</a></li>
//  			<li><a href="{% url '加類型表表格' %}">新增類型</a></li>
//  			<li><a href="{% url '加原始語料表表格' %}">新增語料(地區，年齡，性別，ID)</a></li>
//  			<li><a href="{% url '顯示原始語料表' %}">顯示所有原始語料</a></li>
//  			<li><a href="{% url '上傳檔案' %}">上傳檔案</a></li>
  			
	.config(function($interpolateProvider) {
		/* 解決 Django 和 AngularJS共用{{}}的混淆問題 */
		$interpolateProvider.startSymbol('{$');
		$interpolateProvider.endSymbol('$}');
});