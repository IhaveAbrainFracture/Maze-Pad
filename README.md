# Maze-Pad made by @TheVirtuoso on slack, Vikas IRL
A general spin on a macro-pad, with a fully customised case, PCB, and Firmware. It should also be fully assemblable and useable less than 20 mins after getting everything

<img width="400" height="380" alt="Screenshot 2025-07-12 121642" src="https://github.com/user-attachments/assets/d27cb808-3dae-4643-a974-1ec60397d090" />
<img width="400" height="390" alt="Screenshot 2025-07-12 121719" src="https://github.com/user-attachments/assets/666b0627-b9bd-476d-a23f-5755f4740f37" />


Here is the full cad model to view before you download anything or want a deeper look
https://cad.onshape.com/documents/6287fe38e10122eb28751222/w/de1210ab97eae6cc3d55f10b/e/6d662cd5a03a31552cd37cf9?renderMode=0&uiState=6871c3cb6e1d2f4d0885fcee


# sob story/ why im making this
im a broke highschool student while simultaniously being the youngest in my family often what this mean is all  (if not most) of the technology i own is either a hand-me-down, something i bought myself or something i 'borrowed without the intention of returning' to prove this point want to guess what my current keyboard and mouse look like? Wrong its one of those chunky school keyboard and mice combos that your school bulk buys for there comp room. aside i rly needed an upgrade so i decide to stop being a lazy and work on something. further down the line i also plan on making a keyboard so i kind of treated this as a 'test' run so i could learn the ropes and all

# Specification /cool gimicks (software)
- fully custom code (ie i didnt just yoink the hackpad guide code and make some tweaks)
- 4 macros ( Copy,Paste,Save and alt tab)
- 2 light control buttons ( change in colour, change in pattern)
- 1 layer (I plan on making this 2 layer or more in the future)

 # Specification /cool gimicks (Electronics)
  - wired in a 2x3 matrix
  - custom pcb with funni silk image
  - 2 leds (Neo pixels) which are poorly spaced apart
  - Hopefully smd mounted Xiao
  - diodes at the back

# Specification /cool gimicks (Mechanical)
- fully custom case which doesnt require screws, Bolts or glue (i designed the case based on cool woodworking stuff)
- 7 fully custom mazes for your ADHD
- Custom Maze themed keycaps
- Groves on the side
- maximum fillets
- high mounted cover (this is on purpose i swear, its so it fits my stuff)
- crude hole to look over your enslaved xiao
- backlighting
- funni logos and names
- its black, and white

# general pictures


# instruction to build
ngl if ur building this ur either chonicaly lazy or are collecting hackpads liek infinity stones cos like it cannot be that hard to build your ow. *Aside*
1.plug in your xiao and hold the boot button (clickty clackity on the right) then move the entire firmware folder into the xiao
2.assemble the easy stuff ie the keycaps and put them of the switches
3.place the pcb and all soldered part attacked to it into the main bases (the chunky 3D print)
5. in the allocated slot add the side connector thing thats white and the other white part, for the small bridge if u want the random logoing i put use that side if not rotate it 180 and place it
6. place the case lid and test
7. place small bearing balls into all the mazes
8. done


# bill of mats

| Item | Ammount |From where|
| ------------- | ------------- |----------|
|  mx switches x6  |  |from hackpad kit (i need one of the kits btw)|
|Seeed XIAO RP2040 x1 ||("")|
|SK6812 MINI-E LEDs x2 ||("")|
|3D Printing| none|Printing legion|
|PCB|$18|JLPCB <img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/984df046-567e-444d-95e3-150a55261df8" /> |
|Solder Iron|??|???|
|Flux|$1.53|"https://www.aliexpress.com/item/1005008783332875.html?spm=a2g0o.productlist.main.15.eab81f2bCFhjVT&algo_pvid=45cc1b00-6bcf-43ca-b888-5c4e79205a33&algo_exp_id=45cc1b00-6bcf-43ca-b888-5c4e79205a33-14&pdp_ext_f=%7B"order"%3A"231"%2C"eval"%3A"1"%7D&pdp_npi=4%40dis%21AUD%217.41%211.53%21%21%2134.52%217.16%21%40212e508d17522305550312149ef5c6%2112000046648707772%21sea%21AU%210%21ABX&curPageLogUid=8c35HYaTwcCc&utparam-url=scene%3Asearch%7Cquery_from%3A"|
|Solder|$1.53| https://www.aliexpress.com/item/1005007703287757.html?spm=a2g0o.productlist.main.12.65f06325LWNWpv&algo_pvid=0f0b2a51-30e8-41ca-9b4d-5341719839aa&algo_exp_id=0f0b2a51-30e8-41ca-9b4d-5341719839aa-11&pdp_ext_f=%7B"order"%3A"3030"%2C"eval"%3A"1"%7D&pdp_npi=4%40dis%21AUD%216.45%211.53%21%21%2130.03%217.13%21%400b1bf20817522311015765496e776c%2112000041915671265%21sea%21AU%210%21ABX&curPageLogUid=g3sCp5CWQzIl&utparam-url=scene%3Asearch%7Cquery_from%3A|
