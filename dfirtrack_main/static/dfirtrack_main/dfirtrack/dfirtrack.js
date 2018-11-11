function lastpage() {
    window.history.back();
}

window.onunload = refreshParent;
function refreshParent() {
    window.opener.location.reload();
}

function window_close() {
    window.close()
}

var systemstatuss_add_popup;
function systemstatuss_add_popup() {
    systemstatuss_add_popup = window.open("/systemstatuss/add_popup", "systemstatuss_add_popup", "height=600, width=1000");
}

var analysisstatuss_add_popup;
function analysisstatuss_add_popup() {
    analysisstatuss_add_popup = window.open("/analysisstatuss/add_popup", "analysisstatuss_add_popup", "height=600, width=1000");
}

var reasons_add_popup;
function reasons_add_popup() {
    reasons_add_popup = window.open("/reasons/add_popup", "reasons_add_popup", "height=600, width=1000");
}

var recommendations_add_popup;
function recommendations_add_popup() {
    recommendations_add_popup = window.open("/recommendations/add_popup", "recommendations_add_popup", "height=600, width=1000");
}

var systemtypes_add_popup;
function systemtypes_add_popup() {
    systemtypes_add_popup = window.open("/systemtypes/add_popup", "systemtypes_add_popup", "height=600, width=1000");
}

var ips_add_popup;
function ips_add_popup() {
    ips_add_popup = window.open("/ips/add_popup", "ips_add_popup", "height=600, width=1000");
}

var domains_add_popup;
function domains_add_popup() {
    domains_add_popup = window.open("/domains/add_popup", "domains_add_popup", "height=600, width=1000");
}

var oss_add_popup;
function oss_add_popup() {
    oss_add_popup = window.open("/oss/add_popup", "oss_add_popup", "height=600, width=1000");
}

var companys_add_popup;
function companys_add_popup() {
    companys_add_popup = window.open("/companys/add_popup", "companys_add_popup", "height=600, width=1000");
}

var locations_add_popup;
function locations_add_popup() {
    locations_add_popup = window.open("/locations/add_popup", "locations_add_popup", "height=600, width=1000");
}

var serviceproviders_add_popup;
function serviceproviders_add_popup() {
    serviceproviders_add_popup = window.open("/serviceproviders/add_popup", "serviceproviders_add_popup", "height=600, width=1000");
}

var contacts_add_popup;
function contacts_add_popup() {
    contacts_add_popup = window.open("/contacts/add_popup", "contacts_add_popup", "height=600, width=1000");
}

// show btn-top when 20px are scrolled down
window.onscroll = function() {show_button()};

function show_button() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("btn-top").style.display = "block";
    } else {
        document.getElementById("btn-top").style.display = "none";
    }
}

// got to top on click of button
function go_to_top() {
    document.body.scrollTop = 0; // Safari
    document.documentElement.scrollTop = 0; // Chrome and Firefox
}
