$(document).ready(function(){
	appenddata = ''
	
  $.ajax({
      url:"/getallluggages", 
      type: "post", 
      dataType: 'json',
      data: {},
      beforeSend: function(){
            $(".loader").show();
        },
        success: function(output){
          for(var i=0; i<= output.length-1; i++){
            if (output[i]["status"] == 'open'){
              status =  `<span class="badge rounded-pill bg-primary">Open</span>`
            }else if (output[i]["status"] == 'progress'){
              status =  `<span class="badge rounded-pill bg-warning">Progress</span>`
            }else{
              status =  `<span class="badge rounded-pill bg-success">Delivered</span>`
            }
          	appenddata += `<tr>
            <td>LUG - `+output[i]["luggage_id"]+`</td>
            <td>`+output[i]["from_branch"]+`</td>
            <td>`+output[i]["to_branch"]+`</td>
            <td>`+output[i]["present_hub"]+`</td>
            <td>`+status+`</td>
          </tr>`
          }
         
          $("#luggagedetails").html(appenddata)
          
        },
        error:function(){
          $(".loader").hide();
          alert("Something went wrong! Please try again.")
        }
	});
  
});