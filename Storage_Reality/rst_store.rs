use std::io;


fn real_chk(diff: f32){
    if diff == 0.0{
        println!("You got pranked.");
    } 
    else if diff > 0.0{
        println!("Reality check, its not {value}!!\nIts {reality} GB!", 
        value = diff,
        reality=diff*0.9313226);
    }
    else{
        println!("Wut");}
}

fn main()
{
    println!("How much storage do you have? ");

    let mut storag = String::new();
          io::stdin().read_line(&mut storag).expect("Unable to read entered data");
    let storag: f32 = storag.trim().parse().ok().expect("Program processes numbers only");

    real_chk(storag);
}
