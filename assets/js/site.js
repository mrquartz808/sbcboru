(function(){
  var $=function(s,c){return (c||document).querySelector(s)},$$=function(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s))};
  var safe=function(f){try{return f()}catch(e){}};

  /* sticky header */
  var h=$('.hdr');
  function onScroll(){if(!h)return;h.classList.toggle('stuck',window.scrollY>24);var bg=$('.hero-bg');if(bg&&window.scrollY<900)bg.style.transform='translateY('+(window.scrollY*0.06)+'px)'}
  onScroll();window.addEventListener('scroll',onScroll,{passive:true});

  /* mobil menü */
  var m=$('.mnav');
  $$('.burger').forEach(function(b){b.addEventListener('click',function(){m.classList.add('open');document.body.style.overflow='hidden'})});
  $$('.mnav .x').forEach(function(b){b.addEventListener('click',function(){m.classList.remove('open');document.body.style.overflow=''})});

  /* kategori çekmecesi (mobil) */
  $$('[data-toggle]').forEach(function(b){b.addEventListener('click',function(){var t=$(b.dataset.toggle);if(t)t.classList.toggle('open')})});

  /* fade-up */
  var io='IntersectionObserver' in window?new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12}):null;
  $$('.fu').forEach(function(el){io?io.observe(el):el.classList.add('in')});

  /* sayaç */
  var co='IntersectionObserver' in window?new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;co.unobserve(e.target);var el=e.target,to=parseFloat(el.dataset.to),pre=el.dataset.pre||'',suf=el.dataset.suf||'',t0=null;
    function step(t){if(!t0)t0=t;var p=Math.min((t-t0)/1400,1),v=Math.round(to*(1-Math.pow(1-p,3)));el.textContent=pre+v+suf;if(p<1)requestAnimationFrame(step)}requestAnimationFrame(step)})},{threshold:.4}):null;
  $$('[data-to]').forEach(function(el){if(co)co.observe(el)});

  /* marquee: içeriği ikile */
  $$('.marq-t').forEach(function(t){t.innerHTML+=t.innerHTML});

  /* lightbox */
  var lb=$('.lb');
  $$('[data-lb]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();$('img',lb).src=a.getAttribute('href');lb.classList.add('open')})});
  if(lb)lb.addEventListener('click',function(){lb.classList.remove('open')});

  /* modallar */
  $$('[data-modal]').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();var md=$('#'+b.dataset.modal);if(!md)return;var t=$('[data-mt]',md);if(t&&b.dataset.title)t.textContent=b.dataset.title;md.classList.add('open')})});
  $$('.modal').forEach(function(md){md.addEventListener('click',function(e){if(e.target===md||e.target.closest('.x'))md.classList.remove('open')})});

  /* teklif listesi (localStorage; kapalıysa bellekte) */
  var mem=[];
  function load(){return safe(function(){return JSON.parse(localStorage.getItem('sbc_q')||'[]')})||mem}
  function save(a){mem=a;safe(function(){localStorage.setItem('sbc_q',JSON.stringify(a))})}
  function count(){var n=load().reduce(function(s,i){return s+i.q},0);$$('.cart .cnt').forEach(function(c){c.textContent=n})}
  count();
  $$('[data-add]').forEach(function(b){b.addEventListener('click',function(){var a=load(),id=b.dataset.add,f=a.filter(function(i){return i.id===id})[0];if(f)f.q++;else a.push({id:id,name:b.dataset.name,img:b.dataset.img,q:1});save(a);count();var o=b.innerHTML;b.textContent='Listeye eklendi ✓';setTimeout(function(){b.innerHTML=o},1400)})});
  var ql=$('#qlist');
  if(ql){render()}
  function render(){var a=load();if(!a.length){ql.innerHTML='<div class="empty"><svg class="ic"><use href="#i-quote"/></svg><h4>Teklif listeniz boş</h4><p>Ürünler sayfasından listeye ürün ekleyerek teklif isteyebilirsiniz.</p><a class="btn btn-primary" href="urunler.html">Ürünleri İncele</a></div>';return}
    ql.innerHTML=a.map(function(i,k){return '<div class="row-q"><div class="th"><img src="'+i.img+'" alt=""></div><div><h4>'+i.name+'</h4><div class="small">Kod: SBC-0000 (yer tutucu)</div></div><div class="qty"><button data-d="-1" data-k="'+k+'" aria-label="Azalt">−</button><input value="'+i.q+'" readonly><button data-d="1" data-k="'+k+'" aria-label="Arttır">+</button></div><button class="x-btn" data-r="'+k+'" aria-label="Kaldır"><svg class="ic sm"><use href="#i-close"/></svg></button></div>'}).join('');
    $$('[data-d]',ql).forEach(function(b){b.onclick=function(){var a=load(),it=a[b.dataset.k];it.q=Math.max(1,it.q+parseInt(b.dataset.d));save(a);count();render()}});
    $$('[data-r]',ql).forEach(function(b){b.onclick=function(){var a=load();a.splice(b.dataset.r,1);save(a);count();render()}})}

  /* form doğrulama (statik demo) */
  $$('form[data-demo]').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();var ok=true;
    $$('.fld',f).forEach(function(w){var i=$('input,select,textarea',w);if(!i||!i.required)return;var bad=!i.value.trim()||(i.type==='email'&&!/^\S+@\S+\.\S+$/.test(i.value));w.classList.toggle('err',bad);w.classList.toggle('ok',!bad);if(bad)ok=false});
    if(ok&&f.dataset.demo)location.href=f.dataset.demo})});
})();
