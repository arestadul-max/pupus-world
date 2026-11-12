# Art bible · Rongpat style

## Look
- **Rongpat (Bengali folk art):** bold ink outlines (`#1C1410`), flat colour, paper-theatre depth (layers in front of and behind the characters), no gradients on characters.
- **Palette:** Lampblack `#1C1410`, Conch `#FBF5E9`, Old paper `#F3E6C8`, Sindoor `#C8341F`, Terracotta `#B5482A`, Turmeric `#E3A92B`, Marigold `#E07A2E`, Indigo `#2C3E8C`, Monsoon teal `#1F7A78`, Leaf `#3E7A3A`, Lotus `#E58BA0`.
- **Faces:** one long almond "fish" eye in profile, lively brows, a talking mouth flap, blinking.
- **Setting:** rural Bangladesh: river ghats, tin roofs, banyan and mango trees, lungi, panjabi, tupi, kantha quilts, hurricane lanterns. No Hindu religious motifs.
- **Fonts:** Rozha One (titles), Hind Siliguri (Bangla and body text).
- **Lighting:** the mood decides the light: warm lamp pools and deep shadow at night (Dadu's room, the stairwell), golden hour in memories, grey and faded in the ghat until the first memory brings the colour back.

## Trees (never boring: no flat ellipses, no plain rectangle trunks)
- **Trunk:** thick and tapered, with **flared roots** spreading at the ground and **two or more big limbs** forking up into the canopy. Draw bark as a few long dark curving strokes, not a pattern.
- **Trunk lighting:** dark base colour (`#3E261A`), shadow on the side away from the light, and a strong **warm rim on the lit side** (orange `rgba(236,140,62,.8)` when a lamp is near). The trunk tells you where the light is.
- **Canopy:** built from many (40+) **scalloped leaf clumps** (a centre circle with 7 small circles round its edge), sorted top to bottom, in **four layers**:
  1. a near-black base (`#0C2220`) offset down for depth and edge,
  2. the main green (`#17402E`),
  3. a lighter green (`#24613A`) on the upper clumps, shifted up and left,
  4. small **leaf-top highlights** as flat ellipses (yellow-green `#96BA4A` when lit, cooler `#46803E` in moonlight) only on the top clumps.
- Avoid round highlight dots; they read as polka dots. Highlights sit on the tops of clumps.
- Vary the kind: mango and banyan (broad canopy), krishnachura (red-orange bloom clusters), coconut palm, bamboo. Mix sizes and put some behind fences or buildings (darker, no highlights) and one hero tree near the action (lit).
- Hiding trees must stay wide enough at the trunk (half-width about 35-40 px) to cover Pupu.

## Environments (layers and life)
- Build every scene **back to front**: sky gradient → stars, moon or sun with a **halo** → soft cel-shaded clouds (moving with slow parallax) → far town blocks or tree line (dark, a few tiny lit windows, slow parallax) → main buildings → fence or wall → props → characters → **dark foreground leaves** at the bottom edge (never over the players).
- **Buildings:** flat roofs with a parapet, rooftop details (water tank, stair hut, railing), window rows with a mix of **lit (warm gradient, mullion, small glow)** and dark windows, floor bands.
- **Fences and walls:** capped posts, a top rail with a highlight, a semi-transparent **diamond mesh**, creepers climbing some posts, bushes along the foot. Brick walls get a coping, mortar lines, a few odd bricks, a taped notice, ivy.
- **Props tell the story:** benches, bins, a basketball hoop, a swing, an oil drum, stacked tyres, a name board, posters. Give each a highlight and a shadow ellipse on the ground.
- **Ground:** a paved path with a lit edge and joints, a curb, then a grass verge. Never one flat colour band.

## Lighting recipes
- **Night palette:** deep blue sky (`#0A1238` → `#2C3C84` at the horizon) against **warm gold** lamps and windows. The warm/cool contrast is the mood.
- **Street lamp:** a curved arm, a small bright bulb, a radial **halo** at the bulb, a soft **cone** (additive, fading downward) and an elliptical **pool of light** on the ground. Light the fence, trunks and leaves that sit inside the cone.
- **Lit windows** throw a small additive glow; **lamps and lanterns** throw pools; the moon gets a large faint halo.
- Indoors at night: light shafts from windows, a warm pool where the lamp is, a soft-light grade and a **vignette** so the lit area holds the eye.
- Use `globalCompositeOperation = 'lighter'` for light, low alpha, big radial gradients; use dark multiply-like fills for shadow. Characters stay flat-coloured; light goes on the world.

## Game feel
- **No sliding:** every walk and run is a real step cycle whose cadence matches the speed.
- **Nothing floats:** objects stand on something; plants grow from soil.
- **Doors** have plain panels and a handle, never an emblem.
- **Everything with a seat can be sat on.**
- **Checkpoints are sparse**, so each part stays a challenge.

## Messages on screen
- All instructions appear **above Pupu's head**, one at a time: the use pop-up, then the first-steps tutorial, then button chips, then Pupu's thoughts, then the goal line.
- The **goal line** (a torn notebook page) says what to do, where, and with which button, with an arrow showing the way; it reappears when the player stands still or walks the wrong way.
- The object Pupu has to use **glows softly in its own shape**: a gold halo around its outline only. Never fill or wash the object white; it keeps its own colours with a faint warm tint and a soft rim.
- After a mistake, a **short tip** explains what went wrong and which button helps.
- Controls taught in the Prologue are not taught again later; only new controls get button pop-ups.
- One language at a time: everything in English, or everything in Bangla.

## v265 · Chapter 3 lab art pass (after the user's reference picture)
- Every room has stone-block walls in its own colour (blue-grey ground floor, warm loft, rust-brick machine room, blue upper hall, purple control room and reactor core, warm secret room), drawn only where the camera looks.
- Hanging dome lamps with a metal shade, a warm bulb and a soft cone of light (ground floor, loft, machine room, upper hall, control room, secret room).
- Ivy and hanging vines along ledges and the roof corners; potted plants (ground floor corners, on the bench, by the lift, reactor room corner, control room).
- Purple neon tubes on the reactor room walls; the upper hall back wall shows the night jungle through it; the glass tank has diagonal reflections and a small satellite dish on top.
- Kalo-Bijli's desk with two computers and a chair in the control room; the secret room cover is a plain door marked K-B.
- Outside: jungle silhouettes behind the roof and at both sides, dark earth and bushes below, a thick dark outline around the building; rubble in the dark machinery space.

- **Dadu's chest (v271):** carved teak chest with iron bands and studs and a carved rosette, red velvet inside with ten shaped hollows, quilted lid lining; never any writing on it. Drawn in 3/4 view (v273): the lid is hinged at the back and swings up and back to open, never slides or pops.


## Dadu's storybook (v277)
Brown leather cover (#7A4A26) with a darker inset border (#4A2A16), a gold four-pointed star in the middle (#E8B53A), cream page edges. Held against the chest when carried; held open at chest height to read (cover and star still facing us, the pages fanned up towards him, never over his face), head tipped down; both arms forward to place it.

Book animation set (v279, from the user's sheet): hold · read (pages turning) · close (snap) · walk/run/jump holding it · use (arms forward, gold rays) · place (laid down flat). The book is drawn with its spine away from Pupu and the pages opening at the top towards him.
