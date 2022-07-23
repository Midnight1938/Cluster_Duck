use std::io;

fn expo_calc(time: i32){
    if time == 0 {
        println!("The time was taken as 0.\nYou are dead, congrats.");
    }
    else if time > 0{
        println!("The explosion was within a {} meter radius.",time*343);
    }
    else{println!("You are dead.");}
}


fn lit_calc(diff: i32){
    if diff == 0{
        println!("Youre in it, either watch or seek shelter");
    }
    if diff > 0{
        println!("You are {} meters from the storm. Good luck",diff*343);
    }
    else{println!("Wut");}
}


fn main() {
    println!("Hi! Count the seconds btwn when you saw the light and the sound first. Or guess, no ones judging\n");
    println!("What do you want to calculate?\n1. Explosion\n2. Lightning\n3. Quit");

    println!(":>");
    let mut choice = String::new();
          io::stdin().read_line(&mut choice).expect("Unable to read entered data");
    let choice: i32 = choice.trim().parse().ok().expect("Program processes numbers only");


    if choice == 1 {
        println!("What was the time diffrence between the cloud and the kaboom?");
        let mut explo_tim = String::new();
        io::stdin().read_line(&mut explo_tim).expect("Unable to read entered data");
        let explo_tim: i32 = explo_tim.trim().parse().ok().expect("Program processes numbers only");

        expo_calc(explo_tim);
    } else if choice == 2{
        println!("What was the time btwn flash and thunder?");
        let mut flash_thun_tim = String::new();
        io::stdin().read_line(&mut flash_thun_tim).expect("Unable to read entered data");
        let flash_thun_tim: i32 = flash_thun_tim.trim().parse().ok().expect("Program processes numbers only");

        lit_calc(flash_thun_tim);
    } else { println!("SOmething went wrong ☹️")}
 
}

