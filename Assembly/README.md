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
