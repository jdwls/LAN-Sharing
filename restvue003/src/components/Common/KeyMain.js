export function KeyMain(data){
    let KeyMainChar='2002052820150803'
    let KeyMainlist=KeyMainChar.split('')
    let KeyMainAscll=[]
    let Passwordlist=data.split('') 
    let PasswordAscll=[]
// 密钥转成ASCll码
    for(let i=0;i<=KeyMainlist.length-1;i++){
        KeyMainAscll[i]=KeyMainlist[i].charCodeAt()

        
    }
// 密码转成ASCll码
    for(let i=0;i<=Passwordlist.length-1;i++){
        
        PasswordAscll[i]=Passwordlist[i].charCodeAt()

    }
// 密码补码+到16位
    if(PasswordAscll.length!=16){
        for(let i=PasswordAscll.length;i<=15;i++){
            PasswordAscll[i]=65
            
        }
    }   
//  混淆原来的加密密钥
    for(let i=0;i<=KeyMainAscll.length-1;i++){
        if (KeyMainAscll[i]+i*(16-i)<=127){
            KeyMainAscll[i]=KeyMainAscll[i]+i*(16-i)
        }
        else {
            KeyMainAscll[i]=(KeyMainAscll[i]+i*(16-i))/2
        }  
    }

// 加密数据
    let PasswordCoryBehind=[ ]
    for(let i=0;i<KeyMainAscll.length;i++){
        if(PasswordAscll[i]+KeyMainAscll[i]<=127)
            PasswordCoryBehind[i]=PasswordAscll[i]+KeyMainAscll[i]
        else{
            PasswordCoryBehind[i]=(PasswordAscll[i]+KeyMainAscll[i])/2
        }
    }
// 加密后转Ascll码
    let PasswordCoryBehindAScll=[]
    for(let i=0;i<PasswordCoryBehind.length;i++){
        PasswordCoryBehindAScll[i]=String.fromCharCode(parseInt(PasswordCoryBehind[i]))
    }
// 转成字符串
    let PasswordCoryBehindChar=''
    for(let i=0;i<PasswordCoryBehindAScll.length;i++){
        PasswordCoryBehindChar=PasswordCoryBehindChar+PasswordCoryBehindAScll[i]
    }
    return PasswordCoryBehindChar
    
}
export default KeyMain