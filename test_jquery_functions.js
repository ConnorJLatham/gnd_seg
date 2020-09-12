
$(document).ready(function(){
	$("hide_button").click(function(){
		$("p").hide();
	});
});


$(document).ready(function(){
	$("show_button").click(function(){
		$("p").show();
	});
});



$(function(){
	$("id_button").click(function(){
		$("#test").hide();
	});
});

$(function(){
	$("clas_button").click(function(){
		$(".test").hide();
	});
});