const inputString = "The start of the story is pretty good|Narrator,Benjamin Banana,Amelia Apple|Narrator: As the wind rattled the windowpane, Benjamin Banana looked at his fellow fruit companions with a sparkle in his eyes.Benjamin Banana: 'Do you feel that? Something exciting is about to happen!'Amelia Apple: 'I can't help but feel a sense of anticipation as well. Perhaps this is our chance to break free from the ordinary and embark on a great adventure!'Narrator: The air seemed charged with excitement as the fruits eagerly awaited what the mischievous wind had in store for them.Suddenly, a gust of wind swept through the room, lifting the fruits off the table and carrying them outside.Benjamin Banana: 'Hold on tight, everyone! This is going to be quite a ride!'Amelia Apple: 'Don't worry, we'll stick together and face whatever comes our way!'Narrator: The fruits soared through the sky, their vibrant colors shining against the backdrop of fluffy clouds and the warm glow of the sun.As they traveled higher and higher, they could see a magnificent mountain range in the distance.Benjamin Banana: 'Look, everyone! We're heading towards those beautiful mountains! I wonder what secrets they hold?'Amelia Apple: 'Let's find out! We've come this far, and I have a feeling there's something amazing waiting for us there.'Narrator: With newfound determination, the fruits braved the wind's whims, reaching the majestic mountains at last.As they touched down, they discovered a hidden pathway leading deeper into the mountains.Benjamin Banana: 'Shall we explore, my fruity friends? Adventure awaits just beyond this path!'Amelia Apple: 'Absolutely! Let's see what wonders these mountains have to offer. Who knows, we might find something extraordinary!'Narrator: And so, the fruits began their journey into the unknown, their hearts filled with excitement and curiosity.Where will their path lead them, and what surprises await them in the depths of the mountains?Dear little reader, what do you think lies ahead for our adventurous fruits?";

// Split the input string using pipes
const segments = inputString.split('|');

// Extract individual parts
const storyIntro = segments[0];
const characters = segments[1].split(',');
const storyContent = segments.slice(2).join('|');

// Log the results
console.log('Story Intro:', storyIntro);
console.log('Characters:', characters);
console.log('Story Content:', storyContent);


