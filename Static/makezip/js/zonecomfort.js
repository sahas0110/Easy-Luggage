$(document).ready(function(){

	$.ajax({
      url:"/getopenluggagelist", 
      type: "post", 
      dataType: 'json',
      data: {},
      beforeSend: function(){
            $(".loader").show();
        },
        success: function(output){
          var opt = "<option>Select an option</option>"
          for(var i= 0; i<=output.length - 1;i++){
          	opt += "<option value='"+output[i]["luggage_id"]+"'>LUG - "+output[i]["luggage_id"]+"</option>"
          }
          $("#luggageid").append(opt)
        },
        error:function(){
          $(".loader").hide();
          alert("Something went wrong! Please try again.")
        }
    });

    $("#getdetails").click(function(){
    	let luggageid = $("#luggageid").val()
    	$.ajax({
	      url:"/getluggagedetails", 
	      type: "post", 
	      dataType: 'json',
	      data: {"luggageid":luggageid},
	      beforeSend: function(){
	            $(".loader").show();
	        },
	        success: function(output){
	          $("#frombranch").val(output[0]["from"])
	          $("#tobranch").val(output[0]["to"])
	          var appenddata = ''
	          var notif = ''
	          var pred = ''
	          const d = new Date();
			  let hour = d.getHours() +" : "+d.getMinutes()
	          for(var i=1; i<=output.length-1; i++){
	          	if (output[i]["prediction"] == "fine"){
	          		pred = "Transport route and climate is good"
	          		notif = '<i class="bi bi-circle-fill activity-badge text-success align-self-start"></i>'
	          	}else{
	          		pred = "Transport route and climate is bad"
	          		notif = '<i class="bi bi-circle-fill activity-badge text-danger align-self-start"></i>'
	          	}
	          	appenddata += `<div class="activity-item d-flex">
	                  <div class="activite-label">`+d+`</div>`+notif+`
	                  <div class="activity-content">`
	                   +output[i]["place"]+` : Looks like -`+pred+
	                  `</div>
	                </div>`
	          }
	          $(".activity").html(appenddata)
	        },
	        error:function(){
	          $(".loader").hide();
	          alert("Something went wrong! Please try again.")
	        }
		    });
    	});

});