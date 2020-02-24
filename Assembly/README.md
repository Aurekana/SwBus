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
