# Assembly Guide
Reference numbered images in folder.

## 001. Charge Handle Sub-Assembly
- Cut or print 30ORCUT-ChargePlate. Prototype used lasercut template that was used to cut actual plate from 1/8" steel sheet stock.
- Assemble 07-ChargeHandle onto 30ORCUT-ChargePlate. Prototype was press-fit poorly due to poor fit. Can use adhesive (2-part epoxy) if fit is loose.
- Assemble 08-ChargeLower and 09-ChargeUpper to 30ORCUT-ChargePlate, NOTE POSITIONS IN IMAGE. Also note that 08-ChargeLower and 09-ChargeUpper are not the same height, be sure to assemble in correct positions or else assembly later will require rework.
- Parts were designed with the intent to use a heat-staking process to secure the 08-ChargeLower and 09-ChargeUpper parts into the metal plate, but was rejected due to poor results during assembly. Actual assembly process was to 2-part epoxy plastic parts to metal part, then cut/sand protruding pegs to flush with metal.
- Set assembly aside for later step.

## 002. Grip and Trigger Sub-Assembly
Note: 1/2" aluminum tubes not shown in model. Use as needed for structural reinforcement in 1/2" holes in parts or as shown in assembly steps.
- Assemble 25-Grip to 26-GripBack. Prototype used short length of aluminum tube to reinforce handle.
- Select trigger for use. BOM details prototype trigger, other buttons can be used so long as they are Normally-Open Momentary type and fit in the grip assembly.
- Solder and heatshrink wires to button, leave about 6" or greater wire length off of button for routing.
- Drill/cut opening for button as shown in 002B cross section, hole size depends on button selected.
- Route button wire as shown in 002B cross section. Wire should extend through this hole position.
- Set assembly aside for later step.

## 003. Heat-set Insert Installation
Note: BOM inserts are recommendation, other inserts may be used here with other thread sizes, so long as everything fits or the model is updated for the different inserts. Inserts should not extend beyond hole length into part inside cavities.
- Assemble heat-set inserts to 05-Front and 16-MagFront in positions shown in 003. Prototype process was to heat up soldering iron and push heat-set inserts into holes with heated soldering iron until flush with the surface. Heat was then removed and parts allowed to cool.

## 004. Charge Handle Assembly to Body
- Retrieve Charge Handle sub-Assembly from step 001.
- Measure and cut to length 1/2" aluminum tubing per 004 cross section image - tubes should extend well beyond assembled parts but no less than this length. 
- Test-fit parts and sand/rework as needed so that parts fit smoothly.
- Assemble aluminum tubing into 16-MagFront, then slide on ChargeHandle sub-assembly, followed by 05-Front, followed by 04-Front.
- If all parts fit well, glue 16-MagFront to 05-Front and 04-Front, taking care not to glue ChargeHandle sub-assembly into position unless immobile charge handle desired.

## 005. Magazine Cover Installation
Note: 27-MagCover is also available in the STL folder as 27a-MagCover and 27b-MagCover; this is the 27-MagCover part split into two parts for printers with a not tall enough Z-height. 27a and 27b can be printed separately and fastened together to subsitute for the single part 27. 
- Test fit 27-MagCover into 16-MagFront and 17-MagBack to ensure fit, trim and sand as needed. Prototype required cutting away of a substantial quantity of the shown area of the 27-MagCover to fit under the flap of 17-MagBack.
- Position 27-MagCover into slots on 16-MagFront.
- Insert 3/8" aluminum rod into hole as shown in 005B so that 27-MagCover hinge tabs are secured to 16-MagFront. Ensure 27-MagCover can rotate freely open and closed.
- Assemble 17-MagBack to assembly.

## 006. Front of Stock Installation
- Test fit 18-StockFront to assembly thus far to ensure fit.
- Collect wires to be routed between 18-StockFront and Barrel-Assembly: 2x wires to carry power to the motor (12V, ~1A); 2x wires to carry power to LEDS (5V, ~8A); 1x wire to carry signal to LEDS (5V, <1A)
- Note required routing of power and signal wires in 006B. If path is impossible or obstructed, use a cutting tool or hot knife to cut a slot through the noted path in 006B so that wires can pass and MagCover can still fully close.
- Either route wires through path now, leaving at least 6" on either end outside of the wire path, OR route a cable such that the wire can be pulled along the cable through the wire path during final assembly. If a wire trough was created for routing the wire, skip this step.
- Assemble 18-StockFront to the Overall Assembly.
- Check the area boxed in 006C.
- If a reinforcement tube is present in this location, use a drill or cutting tool to create a hole through the tube so that a wire can be routed in the path shown in 006C.

## 007. Grip Installation
- Retrieve Grip sub-Assembly from step 002. 
- If a hole was drilled through the reinforcement tube during step 006, place a length of heatshrink or anti-abrasion wrap over the trigger button wires to protect them from sharp edges of the aluminum tube.
- Route the trigger button wires through the path shown in the 007 cross section.
- While routing the wires through, assemble the Grip sub-Assembly to the Overall Assembly. Use reinforcement tubes as needed; this handle will be subject to large stresses during carry of the prop.

## 008. Back of Stock Installation
Note: 19-StockBack is also available in the STL folder as 19a-StockBack and 19b-StockBack; this is the 19-StockBack part split into two parts for printers with a not tall enough Z-height. 19a and 19b can be printed separately and fastened together to subsitute for the single part 19.
- Assemble 19-StockBack to the Overall Assembly. The prototype used a single aluminum tube through the lower reinforcement hole; two additional holes were designed in if needed.
- Acquire two neodymium magnets ~12mm diameter by ~3mm tall.
- Sand one face of each magnet to improve adhesion to the nickel plating.
- Glue magnets into the slots in the 19-StockBack as shown in 008.

## 009. Front Support Arm Installation
- Cut two lengths of aluminum 1/2" tube to fit between 01-Front and 02-Front, to act as supports for the 2x Nylon Sleeve Bearings as shown in 009. Assemble the Sleeve Bearings on the aluminum tube, assembling 01-Front to 02-Front.
- Assemble the 01-Front/02-Front assembly to the Overall Assembly.
Note: Nylon Sleeve Bearings designed to rotate freely to support rotating barrel assembly above. In prototype, bearings were accidentally glued into place, so were instead used as a low friction bearing surface.

## 010. Slip Ring Assembly
Note: Alternative slip ring can be used at your own risk.
- Acquire and assemble PCB as described in PCB folder.
- Acquire slip ring with 12 wires, each rated at 2A. 
- Locate +5V, GND, and Signal D_in connection points on PCB.
- Separate out, trim to length, and solder to the PCB 5x wires to the +5V connection point.
- Separate out, trim to length, and solder to the PCB 5x wires to the GND connection point.
- Separate out, trim to length, and solder to the PCB 2x wires to the D_in/Signal connection point.
- Add spacer pad of scrap foam between the Slip Ring flange and PCB to allow even contact despite components on the underside of the PCB. If gluing the PCB to the flange at this step, make sure holes are ligned up as best as possible for later screw mounting.

## 011. Motor Mount Bearing
Note: Different motor can be used, though 21-MotorMount screw attachment points may need to be altered.
- Locate 21-MotorMount.
- Locate Pololu Gearmotor. 
- Assemble 21-MotorMount to top of Pololu Gearmotor using 6x M3 x 6mm long flathead screws. 
- Assemble Ball-Bearing to Motor Assembly.

## 012. Gear Ring Assembly
- Press-fit 24-Ring1 onto the Motor Assembly Ball Bearing. If 24-Ring1 does not fit tightly, wrap tape around the bearing until a tight fit is present.
- Test fit 22-GearRing into the slots in 24-Ring1 to ensure tight fit. 
- Glue 22-GearRing onto 24-Ring1, taking extra care NOT to get glue onto the Ball Bearing.
- If the fit between 22-GearRing and 24-Ring1 is loose, use a bead of hot-glue on the outside of the joint to avoid allowing glue into the Ball Bearing.

## 013. Gear Assembly
- Press-fit 20-Gear onto the D-shaped Motor shaft, taking care to align the D-shaped hole in 20-Gear with the D-shaped shaft. If the 20-Gear does not fit well, sand or file the hole until a good press-fit is achieved. No glue should be necessary, but can be added if a loose fit is present. Avoid getting glue into the Motor.
- Assemble 3x M3 x 3.8mm long heat-set inserts into 32-A as shown in 013 using a heated soldering iron to press the inserts until they are flush with the surface of the part.
- Press-fit 32-A onto the protrusions of 22-GearRing on the Motor Assembly. Glue should not be needed here even in the case of a loose fit.
- Ensure 24-Ring1 rotates smoothly. If movement is not smooth, check for debris or print errors in the 20-Gear and 22-GearRing interface, file down or re-print if needed.

## 014. Slip Ring Wire Routing
Note: Ignore the light blue component in this image; this part will be referenced in the next step.
- Route the wire bundle from the flange (free) end of the slip ring through the hole in 21-MotorMount as shown in 014. For ease of assembly, prior to routing the wire through the 21-MotorMount, add heatshrink around the entire bundle to keep the wires in place. Also add a short length of Nylon anti-abrasion wrap to the wire bundle closest to the slip ring to avoid damage to the wires due to proximity to the 20-Gear.
- Leave enough free length of wire between the slip ring and 21-MotorMount to allow the slip ring assembly to sit on 32-A.
- Fasten the slip ring assembly to 32-A using 3x M3 x 6mm long screws.

## 015. Motor Sleeve Installation
Note: This is the light blue part referenced in the note in the previous step.
- Connect or solder wires to the copper tabs on the Pololu Motor. Wires should be sized for 12V, ~1A. Wires should be at least 24" long to aid routing.
- Add heatshrink or isolation to Pololu Motor wires to avoid shorting to the motor case or to each other.
- Route Motor wires and Slip Ring wires through center of 29-MotorSleeve as shown in 015, then slide 29-MotorSleeve onto Motor taking care to align slot in 29-MotorSleeve to location of wire bundle exit on 21-MotorMount. 29-MotorSleeve should fit very tightly to the Motor; if not then glue 29-MotorSleeve to the Motor, taking care not to allow glue into the Motor internals.
- Pull wires taut through hole in free end of 29-MotorSleeve.

## 016. Cantilever Tube Install
- Acquire Cantilever Tube. Tube should be hollow with a 20mm OD, and be about 325mm in total length. Prototype used thick walled aluminum tube, steel tube could also be used so long as it is strong enough to hold the weight of the barrel assembly cantilevered out from the prop body.
- Route the Slip Ring wires and Motor wires through the center of the Cantilever Tube out the end of the Tube. If the Slip Ring wires are not long enough: acquire 2x wires rated to 5V, 8A; and one wire rated to 5V, ~1A (should be long enough to extend out the end of the Cantilever Tube). Separate out the 5x wires that were connected to the +5V connector on the PCB and connect them to one of the 5V-8A wires. Separate out the 5x wires that were connected to the GND connector on the PCB and connect them to the other 5V-8A wire. Seperate out the 2x wires that were connected to the Signal/D_in connector on the PCB and connect them to the 5V-1A wire. Cover all wire connections with heatshrink to avoid shorting to each other or to the Cantilever Tube body.

## 017. Cylinder Install
- Acquire 23-Cylinder. Note that part has a flat end and a stepped, counterbored end. Reference 017.
- Assemble 23-Cylinder to Motor Assembly such that the stepped, counterbored end is facing the Slip Ring. This stepped end should fit around the Ball Bearing that is fitted into 24-Ring1.

## 018. Ball Bearing Installation
- Press fit a Ball Bearing into 14-Ring2. If fit is loose add tape to outside of bearing until fit is snug. If using glue, be sure not to allow glue onto sides of Ball Bearing. Following any use of glue, check to make sure Ball Bearing still spins freely.
- Assemble 14-Ring2 and Ball Bearing assembly onto Motor Assembly, so that Ball Bearing is facing toward the free end of the Cantilever Tube. See 018. Ball Bearing should fit tightly onto 29-MotorSleeve; if fit is loose add tape around 29-MotorSleeve until fit is snug.

## 019. Long Cylinder Installation
Note: 11-Cylinder and 12-Cylinder are the same part but numbered differently to avoid confusion in needing 2x of one part. They can be printed as one single length if a printer with sufficient Z-height is available.
- Assemble 11-Cylinder and 12-Cylinder to the Motor Assembly as shown in 019. For Prototype assembly 3x lengths of 1/2" nylon tubing were used spaced around the Motor Assembly in the 1/2" tube slots to stabilize the parts and hold them together instead of gluing the parts together. Once the barrels are all installed to the Barrel Assembly, no glue is needed to hold the inner parts together unless otherwise stated.

## 020. Final Ball Bearing Installation
- Assemble a Ball Bearing into 10-Ring3 as shown in 020.
- Assemble the 10-Ring3 and Ball Bearing assembly onto the Motor Assembly as shown in 020, and position 13-Spacer on the Cantilever Tube to support the Ball Bearing. Fit should be tight, add tape or glue if fit is loose, though avoid glue on the sides of the Ball Bearing. As shown in 020, the 13-Spacer should be flush with the side of the Ball Bearing.
- Assemble 06-Ring4 onto the end of the stack of the Motor Assembly. The Prototype assembly used lengths of 1/2" nylon tubing inserted into the 1/2" tube slots on the cylinders to stabilize and hold together the assembly. 
- This completes the Motor Assembly, which will now be referred to as the Barrel Assembly.

## 021. Barrel Assembly to Body Assembly
- Retrieve Body Assembly from Step 009.
- Retrieve Barrel Assembly from Step 020.
- Press-fit Cantilever Tube into front of Body Assembly as shown in 021. Leave at least a 0.5mm gap between the Barrel Assembly and Body Assembly.
- Test rotate Barrel Assembly to make certain sufficient gap is present between the parts.
- If press-fit is not tight enough, use glue (2-part epoxy used for prototype) to secure Cantilever Tube to Body Assembly. Make certain not to glue rotating parts of Barrel Assembly to Body Assembly or to Cantilever Tube. Test rotate following gluing to ensure function.
- Route wires from Barrel Assembly as shown in 021, using wire guide from Step 006. If wires were routed in Step 006, make connections to Barrel Assembly wires now. 
- Glue or secure wires so that 27-MagCover can close fully.

## 022. Electronics sub-Assembly
- Retrieve part "Mount" (does not have unique number, reference 022A for geometry).
- Press-fit 11x M2 hex nuts into Mount as shown in 022A.
- Assemble Adafruit Trinket M0, Pololu Voltage Regulator, and Pololu Motor Controller as shown in 022B. Use M2 x 8mm long screws to secure boards to Mount. Make certain that screws do not extend into undersides of boards on opposite side of Mount. 

Wire together boards as shown in 022C.
- Wire VReg GND to Trinket M0.
- Wire VReg V_out (5V) to a SPST slide switch, then wire slide switch to Trinket M0 "USB" pin. This switch allows the Trinket M0 to be removed from the LED power circuit in event programming mistake results in attempting to light all the LEDs off of the USB programming cable power supply. This was an issue that came up accidentally during programming of the prototype. During normal operation switch should be in closed position.
- Wire the Trigger Button wires to the Motor Controller Board; wire the center-most connection on the Motor Controller Board to Trinket M0 Pin #1 as shown in 022C.
- Wire the Motor Wires to the center two pins of the Motor Control Board power section as shown in 022C.
- Connect the Bat+ and Bat- wires to both the Pololu Voltage Regulator V_in/GND pins as well as to the Motor Controller V_in/GND pins as shown in 022C. Battery wire harness will be covered in the next step.
- Wire Trinket M0 Pin #0 to the LED Signal/D_in wire.
- Wire Pololu Voltage Regulator V_out (5V) pin to LED 5V wire.
- Wire Pololu Voltage Regulator GND to LED GND wire.

## 023. Battery Wiring Harness
Note: Guide specific to parts in BOM that were used in the prototype. 
- Battery connects to system with XT-60 connector, obtain maie connector to plug into female battery connector.
- Wire + side of connector to fuse holder, add a 2.5A glass fuse. Unconnected end of Fuse is now Bat+.
- Wire - side of connector to wire same length as Fuse wire. Encinnected end of - wire is now Bat-.
- Wire battery to ELectronics Assembly from 022 as shown in 023B.

## 024. Potentiometer Door Installation
Note: These doors are holdovers from the original plan to install a linear potentiometer on the Charge Handle to allow control of the motor speed based on the Charge Handle position. This was ultimately dropped from the prototype, so the wiring guides were not implemented. If a linear potentiometer is desired, one can be installed to the insides of these doors prior to assembly and wires routed to the Motor Control Board. The Motor Control Board page at https://www.pololu.com/product/1363/resources should be able to assist in using a potentiometer instead of a button. Also note that the Charge Handle needs the addition of some sort of nub to make contact with the potentiometer. YMMV.
- Install 04-PotDoor and 15-PotDoor as shown in 024. Use 8x M3 x 6mm long screws to secure doors to Body Assembly.

## 025. Barrel LED Assembly
Note: Pictures for this section and those following TBD.
- Cut ten (10) sections of Nylon 1/2" tubing to between 390mm and 400mm in length. Cut all tubes to same length.
- Drill 1/4" hole in each tube about 25mm from one end.
- Cut LED wire harness so that there is roughly 50-60mm of wire beyond the connector.
- Thread the LED wire harness through the drilled hole so that the connector is on the outside of the tube and the wire ends protrude out the end of the tube. Pull tight so that connector is against the tube and is not allowing the wires to be pulled any further out of the tube.
- Cut a length of NeoPixel strip 36 LEDs long.
- Orient the strip so that the D_in side is in view, and pre-tin the three solder pads on the D_in side.
- Solder the wire harness to the NeoPixel strip - reference the PCB board connection - such that the wires that will connect to the 5V on the PCB connect to the NeoPixel +5V; the wires that will connect to the GND on the PCB connect to the NeoPixel GND; and the wires that will connect to the Signal/D_in on the PCB connect to the NeoPixel D_in pin.
- Correct wiring can be verified by plugging in the wire harness to the PCB and powering on the Electronics Assembly Board with the battery or Trinket M0 USB power supply. Use a test program for the Trinket M0 for all LED testing applications. Test program will be added to the repo TBD.
- Cut a strip of LED Foam (Plastazote) approximately 3mm thick and as wide as the NeoPixel strip.
- Use Hot Glue to glue the LED Foam to the NeoPixel strip, so that it sits right above the LEDs.
- Starting with the free end of the NeoPixel strip, carefully insert the end of the NeoPixel strip into the Nylon Tube at the end closest to the drilled hole. Push the strip in flat and straight until it folds over the wire harness and push it all the way in until the wire harness end of the strip is flush with the front of the tube. The wire harness should tuck under the strip.
- Pull the wire harness connector out of the drilled hole as much as possible, but not so much that it breaks.
- Push the Nylon tube side without the drilled hole into the 1/2" tube slots in the Barrel Assembly. Push barrel in until it bottoms out against the back of the Barrel Assembly. A short length of the Nylon tube should be protruding out of the front of the Barrel Assembly.
- Orient the Nylon Tube so that the drilled hole is facing the Slip Ring.
- Plug the Wire harness connector into the PCB into the connector closest to the Nylon Tube.
- Repeat for the other nine (9) Nylon Tubes.

## 026. Barrel End Cap Installation
- Sort the LED wire harness wires so that they stand near their Nylon Tube.
- Note the slots in 32-B. These slots in the 1/2" tube slots should align with the wire harness wires.
- Push 32-B onto the end of the barrel assembly, using a small spudger or flathead screwdriver to move wires as needed to fit into slots.
- Once 32-B is seated against 32-A, Barrel Assembly is complete. 32B should be press-fit, but can be glued in place if no maintenance is expected to be needed for the LED wire harnesses.

## 027. Battery Cover
- Test fit 31-BatCover on the back of the Body Assembly, over where the battery will sit. 31-BatCover should sit over top of two magnets that were glued into the back of the stock.
- Note that 31-BatCover does not have corresponding holes for its own magnets. This was due to a timing constraint and an error in the mesh that prevented holes from being placed. For the prototype a slot was cut in the 31-BatCover that was larger than the locations of the magnets, and the slot was filled with epoxy putty. Magnets were placed on top of the magnets in the stock, then the cover was pressed into place. The cover was then removed, and the depressions in the epoxy putty were let cure and the magnets glued into them. Be sure to orient the magnets properly before gluing.

## 028. HUD/Sight Screen
- Cut Acrylic hud.dxf and check fit in 33-hud.
- Glue Acrylic hud into 33-hud.
- Cut using diagonal cutters two 10mm sections of nail or stiff wire that fits into holes in 33-hud side. Make sure ends of nail/wire are sharp.
- Insert less sharp ends of nail/wire into 33-hud holes, glue in place.
- Press 33-hud with sharp nail/wire into the side of the Body Assembly where the 33-hud is to be installed.
- Find a drill bit slightly smaller than the nail/wire in 33-hud.
- Drill holes in the side of the Body Assembly using the marks made by the sharp nail/wire.
- Insert 33-hud into the holes, and either adjust for a press-fit if removal is desired, or glue in place.
