$(document).ready(function(){
	appenddata = ''
	$.ajax({
      url:"/getparcelhistory", 
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
            }else if (output[i]["status"] == 'returned'){
              status =  `<span class="badge rounded-pill bg-dark w-100">Returned</span>`
            }else{
              status =  `<span class="badge rounded-pill bg-success w-100">Delivered</span>`
            }
          	appenddata += `<tr>
            <td>PRC - `+output[i]["parcel_id"]+`</td>
            <td>`+output[i]["from_branch"]+`</td>
            <td>`+output[i]["created_at"]+`</td>
            <td>`+status+`</td>
            <td>`+output[i]["to_branch"]+`</td>
            <td>`+output[i]["received_date"]+`</td>
          </tr>`
          }
         
          $("#parcelhistorydetails").html(appenddata)
          
        },
        error:function(){
          $(".loader").hide();
          alert("Something went wrong! Please try again.")
        }
	});
});
