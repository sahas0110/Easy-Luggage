$(document).ready(function(){
	//update userdata
	$.ajax({
      url:"/getuserlist", 
      type: "post", 
      dataType: 'json',
      data: {},
      beforeSend: function(){
            $(".loader").show();
        },
        success: function(output){
          var opt = "<option>Select an option</option>"
          for(var i= 0; i<=output.length - 1;i++){
          	opt += "<option value='"+output[i]["user_id"]+"'>"+output[i]["user_id"]+" - "+output[i]["phone"]+"</option>"
          }
          $("#userphone").append(opt)
        },
        error:function(){
          $(".loader").hide();
          alert("Something went wrong! Please try again.")
        }
    });

    $("#userphone").change(function(){
    	var userphone = $("#userphone").val()
	    $.ajax({
	      url:"/getusername", 
	      type: "post", 
	      dataType: 'json',
	      data: {"userphone":userphone},
	      beforeSend: function(){
	        $(".loader").show();
	      },
	      success: function(output){
		      $("#username").val(output[0]["user_name"])
		  },
		  error:function(){
		    $(".loader").hide();
		    alert("Something went wrong! Please try again.")
		   }
		});
    });

    //update luggage
    $.ajax({
      url:"/getopenlug", 
      type: "post", 
      dataType: 'json',
      data: {},
      beforeSend: function(){
            $(".loader").show();
        },
        success: function(output){
          var opt = "<option>Select an option</option>"
          for(var i= 0; i<=output.length - 1;i++){
          	opt += "<option value='"+output[i]["luggage_id"]+"'>"+"LUG"+" - "+output[i]["luggage_id"]+"</option>"
          }
          $("#openlug").append(opt)
        },
        error:function(){
          $(".loader").hide();
          alert("Something went wrong! Please try again.")
        }
    });
    
    //update branch
    $.ajax({
      url:"/getbranchlist", 
      type: "post", 
      dataType: 'json',
      data: {},
      beforeSend: function(){
            $(".loader").show();
        },
        success: function(output){
          var opt = "<option>Select an option</option>"
          for(var i= 0; i<=output.length - 1;i++){
          	opt += "<option value='"+output[i]["branch_id"]+"'>"+output[i]["branch_name"]+"</option>"
          }
          $("#branchfrom").append(opt)
          $("#branchto").append(opt)
        },
        error:function(){
          $(".loader").hide();
          alert("Something went wrong! Please try again.")
        }
    });

    $("#parcelimage").change(function(){
    	var form_data = new FormData(); 
	      form_data.append('file', $('#parcelimage').prop('files')[0]);
	      $.ajax({
	          type: 'POST',
	          url: '/objcount',
	          data: form_data,
	          contentType: false,
	          cache: false,
	          processData: false,
	          success: function(output) {
	             $("#parcelcount").val(output)
	          },
	      });      
    });

    $("#addluggage").click(function(){
    	var servicemanid = $("#servicemanid").val()
    	var userphone = $("#userphone").val()
    	var username = $("#username").val()
    	var openlug = $("#openlug").val()
    	var branchfrom = $("#branchfrom").val()
    	var branchto = $("#branchto").val()
    	var payamount = $("#payamount").val()
    	var parcelcount = $("#parcelcount").val()

	    $.ajax({
	        url:"/addluggage", 
	        type: "post", 
	        dataType: 'json',
			data: {"parcelcount":parcelcount,"payamount":payamount,"servicemanid":servicemanid, "userphone":userphone, "username":username, "openlug":openlug, "branchfrom":branchfrom, "branchto":branchto },
	        beforeSend: function(){
	            $(".loader").show();
	        },
	        success: function(output){
	        	if (output == 1){
	        		alert("Luggage Details Added")
	        	}
	        },
	        error:function(){
	          $(".loader").hide();
	        }
	    });   
    });

});