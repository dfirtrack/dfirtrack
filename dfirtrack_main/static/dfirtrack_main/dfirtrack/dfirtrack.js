// ####################################
// #
// # generic functions
// #
// ####################################

// go to lastpage (used for cancel button)
function lastpage() {
    window.history.back();
}

// close window (used for cancel popup button to close popup window)
function window_close() {
    window.close()
}

// reload parent page if child page is closed (used when save or cancel button is pushed in popup window or if it is closed)
window.onunload = refreshParent;
function refreshParent() {
    window.opener.location.reload();
}

// ####################################
// #
// # popup window related functions
// #
// ####################################

// popup window for adding company
var companys_add_popup;
function companys_add_popup() {
    companys_add_popup = window.open("/companys/add_popup", "companys_add_popup", "height=600, width=1000");
}

// popup window for adding contact
var contacts_add_popup;
function contacts_add_popup() {
    contacts_add_popup = window.open("/contacts/add_popup", "contacts_add_popup", "height=600, width=1000");
}

// popup window for adding domain
var domains_add_popup;
function domains_add_popup() {
    domains_add_popup = window.open("/domains/add_popup", "domains_add_popup", "height=600, width=1000");
}

// popup window for adding location
var locations_add_popup;
function locations_add_popup() {
    locations_add_popup = window.open("/locations/add_popup", "locations_add_popup", "height=600, width=1000");
}

// popup window for adding operating system
var oss_add_popup;
function oss_add_popup() {
    oss_add_popup = window.open("/oss/add_popup", "oss_add_popup", "height=600, width=1000");
}

// popup window for adding reason
var reasons_add_popup;
function reasons_add_popup() {
    reasons_add_popup = window.open("/reasons/add_popup", "reasons_add_popup", "height=600, width=1000");
}

// popup window for adding recommendation
var recommendations_add_popup;
function recommendations_add_popup() {
    recommendations_add_popup = window.open("/recommendations/add_popup", "recommendations_add_popup", "height=600, width=1000");
}

// popup window for adding serviceprovider
var serviceproviders_add_popup;
function serviceproviders_add_popup() {
    serviceproviders_add_popup = window.open("/serviceproviders/add_popup", "serviceproviders_add_popup", "height=600, width=1000");
}

// popup window for adding systemtype
var systemtypes_add_popup;
function systemtypes_add_popup() {
    systemtypes_add_popup = window.open("/systemtypes/add_popup", "systemtypes_add_popup", "height=600, width=1000");
}

// ####################################
// #
// # go to top of page button
// #
// ####################################

// go to top of page button (onscroll event)
window.onscroll = function() {show_button()};

// go to top of page button (show btn-top if 20px are scrolled down)
function show_button() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("btn-top").style.display = "block";
    } else {
        document.getElementById("btn-top").style.display = "none";
    }
}

// go to top of page button (on click of button)
function go_to_top() {
    document.body.scrollTop = 0; // Safari
    document.documentElement.scrollTop = 0; // Chrome and Firefox
}
