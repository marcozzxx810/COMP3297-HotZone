function objectifyForm(form) {
    var finalObj = { };
    $.each($(form).serializeArray(), function() {
        finalObj[this.name] = this.value;
    });
    return finalObj
}


function submitCaseForm() {
    $("div.error_msg").empty();
    const patientobj = objectifyForm("form.patient");
    const caseobj = objectifyForm("form.case");
    caseobj['patient'] = patientobj;
    var r = confirm('Confirm to submit this case information?\n'+JSON.stringify(caseobj));
    if(r){
        $.ajax({
            url: "/caserecord/",
            data: JSON.stringify(caseobj),
            type: "POST",
            dataType: "json",
            contentType: "application/json;charset=utf-8",
            success: function(returnData){
                $("div.error_msg").append(`<p style="color:green;">${returnData}</p>`);
                $("form.patient").trigger("reset");
                $("form.case").trigger("reset");
            },
            error: function(xhr, ajaxOptions, thrownError){
                $("div.error_msg").append(`<p style="color:red;">${xhr.responseText}</p>`);
            }
        });
    }
}

function lowerFirstLetter(string) {
    return string.charAt(0).toLowerCase() + string.slice(1);
}

function submitSearch() {
    var url = 'https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?'
    if ( ! $("#geoSearch")[0].value ) {
        alert("Please enter location");
        return
    }
    var parms = {'q':$("#geoSearch")[0].value};
    var str = jQuery.param( parms );
    $.getJSON(url+str, function(json){
        if(json.length == 1){
            $.each($("form.locationData")[0], function(){
                value = json[0][lowerFirstLetter(this.name.substring(3))];
                this.value = value;
            })
        } else {
            alert(`GeoData Store return ${json.length} results`);
        }
    }).fail( function(d, textStatus, error) {
        alert("Cannot retrieve Geodata, status: " + textStatus + ", error: "+error);
    });;
}

function clearSearch(){
    $("form.locationData").trigger("reset");
}

function submitLocationRecordForm() {
    $("div.error_msg").empty();
    const locationobj = objectifyForm("form.locationData");
    const locationRobj = objectifyForm("form.locationRecord");
    locationRobj['visitedLoc'] = locationobj;
    var r = confirm('Confirm to submit this virus information?\n'+JSON.stringify(locationRobj))
    if(r){
        $.ajax({
            url: "/visitedlocation/",
            data: JSON.stringify(locationRobj),
            type: "POST",
            dataType: "json",
            contentType: "application/json;charset=utf-8",
            success: function(returnData){
                $("div.error_msg").append(`<p style="color:green;">${returnData}</p>`);
                $("form.locationData").trigger("reset");
                $("form.locationRecord").trigger("reset");
            },
            error: function(xhr, ajaxOptions, thrownError){
                $("div.error_msg").append(`<p style="color:red;">${xhr.responseText}</p>`);
            }
        });
    }
}

function submitVirusForm() {
    $("div.error_msg").empty()
    const virusobj = objectifyForm("form.virus")
    var r = confirm('Confirm to submit this virus information?\n'+JSON.stringify(virusobj))
    if (r){
        $.ajax({
            url: "/virus/",
            data: JSON.stringify(virusobj),
            type: "POST",
            dataType: "json",
            contentType: "application/json;charset=utf-8",
            success: function(returnData){
                $("div.error_msg").append(`<p style="color:green;">${returnData}</p>`);
                $("form.virus").trigger("reset");
            },
            error: function(xhr, ajaxOptions, thrownError){
                $("div.error_msg").append(`<p style="color:red;">${xhr.responseText}</p>`);
            }
        });
    }
}