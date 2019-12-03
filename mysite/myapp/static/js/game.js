///////////// s0
const canvas_s0 = document.getElementById('s0');
const s0 = canvas_s0.getContext('2d');

s0.fillStyle = '#FF0000';
s0.fillRect(0, 0, canvas_s0.width, canvas_s0.height);

///////////// s1
const canvas_s1 = document.getElementById('s1');
const s1 = canvas_s1.getContext('2d');

s1.fillStyle = '#000';
s1.fillRect(0, 0, canvas_s1.width, canvas_s1.height);

///////////// s2
const canvas_s2 = document.getElementById('s2');
const s2 = canvas_s2.getContext('2d');

s2.fillStyle = '#000';
s2.fillRect(0, 0, canvas_s2.width, canvas_s2.height);

/////////////s3
const canvas_s3 = document.getElementById('s3');
const s3 = canvas_s3.getContext('2d');

s3.fillStyle = '#000';
s3.fillRect(0, 0, canvas_s3.width, canvas_s3.height);

/////////////s4
const canvas_s4 = document.getElementById('s4');
const s4 = canvas_s4.getContext('2d');

s4.fillStyle = '#000';
s4.fillRect(0, 0, canvas_s4.width, canvas_s4.height);

/////////////s5
const canvas_s5 = document.getElementById('s5');
const s5 = canvas_s5.getContext('2d');

s5.fillStyle = '#000';
s5.fillRect(0, 0, canvas_s5.width, canvas_s5.height);

/////////////s6
const canvas_s6 = document.getElementById('s6');
const s6 = canvas_s6.getContext('2d');

s6.fillStyle = '#000';
s6.fillRect(0, 0, canvas_s6.width, canvas_s6.height);

/////////////s7
const canvas_s7 = document.getElementById('s7');
const s7 = canvas_s7.getContext('2d');

s7.fillStyle = '#000';
s7.fillRect(0, 0, canvas_s7.width, canvas_s7.height);

/////////////s8
const canvas_s8 = document.getElementById('s8');
const s8 = canvas_s8.getContext('2d');

s8.fillStyle = '#000';
s8.fillRect(0, 0, canvas_s8.width, canvas_s8.height);

/////////////s9
const canvas_s9 = document.getElementById('s9');
const s9 = canvas_s9.getContext('2d');

s9.fillStyle = '#000';
s9.fillRect(0, 0, canvas_s9.width, canvas_s9.height);

/////////////s10
const canvas_s10 = document.getElementById('s10');
const s10 = canvas_s10.getContext('2d');

s10.fillStyle = '#000';
s10.fillRect(0, 0, canvas_s10.width, canvas_s10.height);

/////////////s11
const canvas_s11 = document.getElementById('s11');
const s11 = canvas_s11.getContext('2d');

s11.fillStyle = '#000';
s11.fillRect(0, 0, canvas_s11.width, canvas_s11.height);

////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////
/*
function button0() {
    s0.fillStyle = 'red';
    s0.fillRect(0, 0, canvas_s0.width, canvas_s0.height);
}
*/
function cardTabs(evt, tabName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}