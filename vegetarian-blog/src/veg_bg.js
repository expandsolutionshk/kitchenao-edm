/* B1 KV 背景（Canvas 即時處理，Pexels 圖片支援 CORS）
   底圖 Pexels 5418661：保留原本食物，抹走青蔥、蒜頭換成番茄（去五辛）
   少量加入：紫豆角（Pexels 5202092）、紫羽衣甘藍（Pexels 5755657），均去白底後貼上 */
(function(){
const P=n=>'https://images.pexels.com/photos/'+n+'/pexels-photo-'+n+'.jpeg?auto=compress&cs=tinysrgb&w=';
const LD=async s=>{const i=new Image();i.crossOrigin='anonymous';i.src=s;await i.decode();return i};
function CUT(im,crop){const [cx,cy,cw,ch]=crop.map((v,i)=>v*(i%2?im.naturalHeight:im.naturalWidth));const c=document.createElement('canvas');c.width=cw|0;c.height=ch|0;const x=c.getContext('2d');x.drawImage(im,cx,cy,cw,ch,0,0,c.width,c.height);const d=x.getImageData(0,0,c.width,c.height);const p=d.data;
const Ls=[];for(let i=0;i<p.length;i+=40)Ls.push(.3*p[i]+.59*p[i+1]+.11*p[i+2]);Ls.sort((a,b)=>a-b);const Lb=Ls[Ls.length*0.6|0];
for(let i=0;i<p.length;i+=4){const r=p[i],g=p[i+1],b=p[i+2];const Lm=.3*r+.59*g+.11*b;const mx=Math.max(r,g,b),mn=Math.min(r,g,b);const sat=mx?(mx-mn)/mx:0;let a,obj;const lo=Lb-90,hi=Lb-25;
if(Lm<lo){a=1;obj=1}else if(Lm<hi&&sat>0.10){a=(hi-Lm)/(hi-lo);obj=1}else{obj=0;a=Math.max(0,Math.min(.55,(Lb-Lm)/Lb*2.2))}
if(obj){if(a<1){for(let j=0;j<3;j++)p[i+j]=Math.max(0,Math.min(255,(p[i+j]-(1-a)*Lb)/a))}}else{p[i]=10;p[i+1]=25;p[i+2]=15}p[i+3]=a*255}
x.putImageData(d,0,0);return c}
function EDGE(cv,f){f=f||.12;const c=document.createElement('canvas');c.width=cv.width;c.height=cv.height;const x=c.getContext('2d');x.drawImage(cv,0,0);x.globalCompositeOperation='destination-in';const w=c.width,h=c.height;
[[w,0],[0,h]].forEach(([gx,gy])=>{const g=x.createLinearGradient(0,0,gx,gy);g.addColorStop(0,'rgba(0,0,0,0)');g.addColorStop(f,'#000');g.addColorStop(1-f,'#000');g.addColorStop(1,'rgba(0,0,0,0)');x.fillStyle=g;x.fillRect(0,0,w,h)});return c}
async function EDIT(src){
const [bi,ki]=await Promise.all([LD(P(5202092)+'900'),LD(P(5755657)+'900')]);
const CB=EDGE(CUT(bi,[.05,.15,.92,.75])),CK=EDGE(CUT(ki,[.12,.12,.8,.8]));

const im=new Image();im.crossOrigin='anonymous';im.src=src;await im.decode();
const W=im.naturalWidth,H=im.naturalHeight,k=W/1600;
const c=document.createElement('canvas');c.width=W;c.height=H;const x=c.getContext('2d');x.drawImage(im,0,0);
const S=(a,b)=>[(a-8)*2.381*k,(b-8)*2.381*k];
const m=document.createElement('canvas');m.width=W;m.height=H;const mx=m.getContext('2d');
mx.fillStyle='#fff';mx.beginPath();[[374,0],[690,0],[690,72],[578,82],[472,126],[432,152],[384,154],[372,118],[372,60]].forEach((p,i)=>{const q=S(...p);i?mx.lineTo(...q):mx.moveTo(...q)});mx.closePath();mx.fill();
const g=S(445,232);mx.beginPath();mx.arc(g[0],g[1]+4*k,33*2.381*k,0,7);mx.fill();
const f=8,w=Math.ceil(W/f),h=Math.ceil(H/f);
const sc=document.createElement('canvas');sc.width=w;sc.height=h;const sx=sc.getContext('2d');sx.drawImage(c,0,0,w,h);const sd=sx.getImageData(0,0,w,h).data;
const mc=document.createElement('canvas');mc.width=w;mc.height=h;const mcx=mc.getContext('2d');mcx.drawImage(m,0,0,w,h);const mm=mcx.getImageData(0,0,w,h).data;
const ins=new Uint8Array(w*h);for(let i=0;i<w*h;i++)ins[i]=mm[i*4]>10?1:0;
const ch=[0,1,2].map(j=>{const a=new Float32Array(w*h);for(let i=0;i<w*h;i++)a[i]=sd[i*4+j];return a});
for(const a of ch){let mean=0,n=0;for(let i=0;i<w*h;i++)if(!ins[i]){mean+=a[i];n++}mean/=n;for(let i=0;i<w*h;i++)if(ins[i])a[i]=mean;
for(let it=0;it<500;it++){for(let yy=1;yy<h-1;yy++)for(let xx=1;xx<w-1;xx++){const i=yy*w+xx;if(!ins[i])continue;const v=(a[i-1]+a[i+1]+a[i-w]+a[i+w])/4;a[i]+=1.9*(v-a[i])}
for(let yy=0;yy<h;yy++){const i=yy*w;if(ins[i])a[i]=a[i+1];const j=yy*w+w-1;if(ins[j])a[j]=a[j-1]}for(let xx=0;xx<w;xx++){if(ins[xx])a[xx]=a[xx+w];const j=(h-1)*w+xx;if(ins[j])a[j]=a[j-w]}}}
const fill=document.createElement('canvas');fill.width=w;fill.height=h;const fl=fill.getContext('2d');const fdI=fl.createImageData(w,h);for(let i=0;i<w*h;i++){fdI.data[i*4]=ch[0][i];fdI.data[i*4+1]=ch[1][i];fdI.data[i*4+2]=ch[2][i];fdI.data[i*4+3]=255}fl.putImageData(fdI,0,0);
const big=document.createElement('canvas');big.width=W;big.height=H;const bx=big.getContext('2d');bx.imageSmoothingQuality='high';bx.drawImage(fill,0,0,W,H);const bd=bx.getImageData(0,0,W,H).data;
const fm=document.createElement('canvas');fm.width=W;fm.height=H;const fx2=fm.getContext('2d');fx2.filter='blur('+Math.round(6*k)+'px)';fx2.drawImage(m,0,0);const fd=fx2.getImageData(0,0,W,H).data;
const id=x.getImageData(0,0,W,H);const d=id.data;
for(let i=0;i<W*H*4;i+=4){const a=Math.min(1,fd[i]/255*1.8);if(a<=0.01)continue;const n=(Math.random()-.5)*5;for(let j=0;j<3;j++)d[i+j]=d[i+j]*(1-a)+(bd[i+j]+n)*a}
x.putImageData(id,0,0);
const srcT=S(116,240),R=56*2.381*k,sc2=.62,D=R*sc2;const t=document.createElement('canvas');t.width=t.height=Math.ceil(D*2);const tx=t.getContext('2d');
tx.drawImage(c,srcT[0]-R,srcT[1]-R+4*k,R*2,R*2,0,0,D*2,D*2);tx.globalCompositeOperation='destination-in';const gr=tx.createRadialGradient(D,D,D*.8,D,D,D*.98);gr.addColorStop(0,'#000');gr.addColorStop(1,'rgba(0,0,0,0)');tx.fillStyle=gr;tx.fillRect(0,0,D*2,D*2);
x.drawImage(t,g[0]-D,g[1]-D+4*k);
const put=(cv,cxS,cyS,len,deg,br,fy)=>{const q=S(cxS,cyS);const sc=len*k/Math.max(cv.width,cv.height);x.save();x.filter='brightness('+br+')';x.translate(q[0],q[1]);if(fy)x.scale(1,-1);x.rotate(deg*Math.PI/180);x.drawImage(cv,-cv.width*sc/2,-cv.height*sc/2,cv.width*sc,cv.height*sc);x.restore()};

ADD(put,CB,CK);
return c.toDataURL('image/jpeg',.9)}
function ADD(put,CB,CK){put(CB,470,92,400,72,1.12,1);put(CK,610,112,300,-100,1.25,1)}  /* 第 7 個參數 1 = 上下鏡像 */
const imgs=document.querySelectorAll('img[data-vegbg]');if(!imgs.length)return;
const src=imgs[0].getAttribute('src');EDIT(src).then(u=>imgs.forEach(i=>{i.src=u;i.style.opacity=1})).catch(e=>{console.error(e);imgs.forEach(i=>i.style.opacity=1)});
})();
