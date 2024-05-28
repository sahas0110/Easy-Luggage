$(document).ready(function(){

	$("#addquery").click(function(){
		var subject = $("#subject").val()
		var query = $("#query").val()

		if (subject == ''){
			$("#errormsg").text("Enter the subject!")
			$("#errormsg").css("color", "red")
			$("#errormsg").show()
		}else if(query == ''){
			$("#errormsg").text("Enter the query/feed!")
			$("#errormsg").css("color", "red")
			$("#errormsg").show()
		}else{
			$("#errormsg").hide()
			$.ajax({
		      url:"/addquery", 
		      type: "post", 
		      dataType: 'json',
		      data: {"subject":subject, "query":query},
		      beforeSend: function(){
		          $(".loader").show();
		      },
		      success:function(data){
		      	if (data == 1){
		      		$("#errormsg").text("Thanks for sending us! We contact you shortly")
					$("#errormsg").css("color", "green")
					$("#errormsg").show()
		      	}
		      }
		   });
		}
	});

});
