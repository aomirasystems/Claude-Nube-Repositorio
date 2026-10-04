"""
Net Worth POV - Video 5: "POV: You Said No to Lifestyle Creep - And Your Friends Noticed"
Cifras ilustrativas: take-home sube 150/mes por año (3,500 -> 5,000 en 10 años); Sam gasta fijo 3,000/mes y ahorra la diferencia (650 en año 1 -> 2,000 en año 10), 5% anual -> ~191,000; amigo ahorra 500/mes fijo (6,000/año) a 5% -> ~75,500.
Uso: python netWorthPOV_v5_scenes.py
"""
from nwpov_common import emit

S = []
def sc(kind, setting, visual, narr):
    S.append((kind, setting, visual, narr))

# ---- gancho ----
sc("MACRO", "DESK", "a worn brown leather wallet with one frayed corner and a visible stitch on a dark wooden table, a folded paper napkin and a set of keys beside it, no letters and no digits.",
   "A worn brown wallet sits on a coffee table. It has been in your pocket for ten years.")
sc("SIT", "LIVING", "he sits on the couch holding a glass of water, three small friend silhouettes cropped at the edges of the frame, warm lamplight.",
   "Your three oldest friends are over for dinner. Everyone looks tired in the same way, except you.")
sc("WIDE", "LIVING", "a wide view of the living room, three friend silhouettes slumped on chairs with sighing posture, Sam small in the middle of the couch.",
   "They talk about rent, car payments, and how a good salary somehow still feels tight.")
sc("CLOSE", "LIVING", "his face in close-up, a kind and quiet expression, nodding slightly, soft lamp light.",
   "You nod along. You are not bragging. You are simply doing fine, and you have been quiet about it.")
sc("HAND", "LIVING", "a friend's hand holding up the worn brown wallet toward the camera, a laughing silhouette blurred behind it.",
   "One friend picks up your old wallet and laughs. Ten years, same wallet, same sweatshirt, same plain car.")
sc("CLOSE", "LIVING", "a cropped friend silhouette at the edge of the frame, his face half in shadow, with Sam's attentive face in the foreground.",
   "Then he stops laughing. He asks, very quietly, how you are the only one of us who is not stressed.")
sc("SIT", "LIVING", "he sits on the couch with a gentle smile, looking at the camera, a small clock icon floating beside his head.",
   "You think about the real answer. It is not a secret. It started with one raise, ten years ago.")
sc("MACRO", "CLEAN", "a large flat icon of two left-pointing arrows in a rewind symbol, thick dark outline, centered on a plain cream wall, no text.",
   "So let us rewind to the day your first real raise arrived.")

# ---- acto 2: el punto de partida ----
sc("WIDE", "OFFICE", "he sits tiny at a cubicle in a large open office, one monitor glowing, rows of empty chairs around him.",
   "Ten years earlier you are twenty-seven, working an ordinary office job, and living in a small apartment you can afford.")
sc("SIT", "OFFICE", "he sits across a desk from a manager silhouette cropped at the edge, hands on his knees, a small green upward arrow floating above the desk.",
   "One morning your manager calls you in and announces a raise. For the first time, you feel a little rich.")
sc("HAND", "OFFICE", "a hand holding a smartphone, the screen shows a pale banking app with a small green arrow and gray bars, no readable text and no digits.",
   "It adds about one hundred fifty dollars a month. It is not huge, but it feels like permission.")
sc("WIDE", "STREET", "a trendy downtown loft building with large windows, three small friend silhouettes carrying moving boxes at the entrance, a sleek sports car parked at the curb.",
   "That same year your friends get raises too, and they celebrate by upgrading everything they can.")
sc("STAND", "STREET", "he stands on the sidewalk watching with open curiosity as two friend silhouettes carry boxes into the building, cropped at the edge, a small suitcase icon floating nearby.",
   "One moves downtown. Another leases a sporty car. The third books a vacation every season.")
sc("CLOSE", "KNIGHT", "his face in close-up lit by the cold glow of a phone below the frame, a small wistful half smile.",
   "At night you scroll through their photos and feel a small, familiar tug. Maybe you should upgrade too.")
sc("STAND", "DEALER", "he stands beside a shiny new coupe in a bright dealership showroom, a salesperson silhouette cropped at the edge, a large glossy window behind.",
   "One Saturday you walk into a dealership and sit inside a shiny new car. It smells like possibility.")
sc("HAND", "DEALER", "a hand holding a clipboard with a paper made of gray blurred lines and a pen, a tiny calendar icon in the corner, no readable text and no digits.",
   "The salesperson says the monthly payment is almost nothing, because it is stretched over many years.")
sc("CLOSE", "DEALER", "his face in close-up, eyebrows slightly raised as he works something out, the glow of showroom lights on his cheek.",
   "You do the math in your head, and it is not the payment that bothers you. It is the years.")
sc("WIDE", "STREET", "he walks out of the dealership toward his plain older compact car parked alone in the lot, golden hour light, the glass doors behind him.",
   "You thank him, shake his hand, and walk out. Your old car waits in the lot like a loyal friend.")
sc("SIT", "KNIGHT", "he sits at the kitchen table at night with a notebook and a pencil, one lamp glowing, looking thoughtfully at the camera.",
   "That night you realize something. Your raise did not make your old life too small. It only made it feel smaller.")
sc("MACRO", "DESK", "a flat illustration of a horizontal line drawn across a notebook page with a coin stack above it growing taller, no text and no digits.",
   "You set one rule. Your monthly spending line stays put, adjusted for rising prices. Everything above it goes to the future.")
sc("HAND", "KDAY", "a hand holding a smartphone, the screen shows a flat icon of an arrow moving from a wallet to a small shield, no readable text and no digits.",
   "You set up an automatic transfer, so the extra money moves away before you even see it.")
sc("MACRO", "DESK", "a flat illustration of a small gift box icon and a ticket icon sitting beside a tiny jar, warm light, no text and no digits.",
   "You also keep a small fun fund, so this is a plan and not a punishment.")
sc("SIT", "KDAY", "he sits at the kitchen table with a white mug, looking slightly lonely but calm, morning light, a small left-pointing arrow icon drifting in the window behind him.",
   "It feels a little lonely at first, because everyone around you is moving in the opposite direction.")

# ---- acto 3: los años del medio ----
sc("WIDE", "STREET", "a suburban street where a friend silhouette drives past in a shiny convertible, Sam tiny at the curb with his hands in his pockets.",
   "Over the next few years, your friends upgrade like clockwork. Bigger rent, newer cars, fancier weekends.")
sc("STAND", "STREET", "he stands at his front door politely shaking his head, a cropped friend silhouette holding a pair of ski goggles at the edge of the frame.",
   "They invite you on a ski trip that costs more than your rent. You politely say no.")
sc("CLOSE", "LIVING", "a cropped friend silhouette teasing at the edge of the frame, Sam's face in the foreground with a small, surprised smile.",
   "A friend teases you. You have changed, he says. You used to be fun.")
sc("SIT", "LIVING", "he sits on the couch with a thoughtful face, his hands folded, a faint heart icon floating beside his head.",
   "That stings, because you love your friends. You just do not want to pay for approval.")
sc("HAND", "LIVING", "a hand holding a smartphone, the screen shows a group chat with colorful photo thumbnails and gray bubbles, no readable text and no digits.",
   "The group chat keeps buzzing with photos of dinners and trips. You press like, and you stay home.")
sc("MACRO", "DESK", "a flat illustration of a flat horizontal line with a steadily rising green line above it, no text and no digits.",
   "Every year your pay grows a little, and every year your spending line stays flat.")
sc("SIT", "KDAY", "he sits at the kitchen table calmly sipping from a mug, sunny window, a green plant growing in a small pot beside him.",
   "Your savings are not a fixed number. They grow with every raise, and that is the whole trick.")
sc("MACRO", "DESK", "a flat illustration of coin stacks rising in steps like a staircase from short to tall, no text and no digits.",
   "In year one you save about six hundred fifty dollars a month. By year ten, it is closer to two thousand.")
sc("WIDE", "STREET", "a friend silhouette beside a brand new leased sports car in a driveway, a small stack of bills drawn as gray rectangles at the edge of the frame.",
   "Your friends do the opposite. Each raise gets spent, so their savings stay flat while their bills keep growing.")
sc("CLOSE", "KNIGHT", "his face in close-up at night, calm and kind, soft light.",
   "You are not judging them. You know how easy it is, because the temptation never goes away.")
sc("STAND", "STREET", "he stands in a driveway beside his older compact car with the hood up and a thin wisp of pale smoke rising, hands on hips.",
   "In year four, your old car finally dies, and you need a replacement.")
sc("STAND", "DEALER", "he stands in a modest used car lot beside a clean, plain gray car with a calm smile, a cropped salesperson silhouette at the edge.",
   "This time you buy a reliable used car with cash from your car fund, and nobody throws a party.")
sc("WIDE", "STREET", "he drives away from the used car lot in the plain gray car, two friend silhouettes cropped on the sidewalk waving with mocking smiles.",
   "Your friends tease you about buying used. You drive home smiling, with no payment hanging over you.")
sc("SIT", "OFFICE", "he sits at his cubicle, two coworker silhouettes cropped at the edge, hunched over desks with large clock icons floating above them.",
   "At work, the people who bragged about leases begin taking extra shifts to cover their payments.")
sc("CLOSE", "OFFICE", "a cropped coworker silhouette with tired shoulders at the edge of the frame, Sam's face in the foreground, calm and sympathetic.",
   "You see tired eyes and Sunday night dread, and you quietly thank your younger self.")
sc("MACRO", "DESK", "a flat illustration of a small stack of coins with a green plant growing from it, a faint clock icon behind, no text and no digits.",
   "Five hundred dollars a month, growing about five percent a year, becomes roughly seventy-five thousand dollars in ten years.")
sc("SIT", "KNIGHT", "he sits at the kitchen table at night with a calculator with blank gray keys, a thoughtful look, one lamp glowing.",
   "That is your friend who never stopped upgrading. It is not nothing, but it is not freedom either.")
sc("HAND", "KNIGHT", "a hand drawing a rising green line in a notebook beside a coin icon, no letters and no digits.",
   "Now count your path. Savings that start near six hundred fifty dollars a month and rise with every raise.")
sc("MACRO", "DESK", "a flat illustration of a tall coin stack next to a much shorter coin stack, a small green flag on the tall one, no text and no digits.",
   "In this example, that adds up to roughly one hundred ninety thousand dollars by year ten.")
sc("CLOSE", "LIVING", "his face in close-up, eyes thoughtful, warm light on one cheek.",
   "Same salary. Same city. A gap of more than one hundred thousand dollars, built from a few polite refusals.")
sc("SIT", "LIVING", "he sits on the couch with open hands in a calm gesture, a small cloud and sun icon floating beside his head.",
   "Of course, this is an illustration. Markets move, prices rise, and your friends may catch up later.")
sc("STAND", "STREET", "he stands on a quiet street corner holding a new soft pillow-sized box with a ribbon, a relaxed smile, evening light.",
   "You do upgrade some things. One year it is a great mattress. Another year, a trip you actually plan.")
sc("HAND", "KDAY", "a hand holding a pen over a notebook with a checkmark icon beside a small heart icon, no letters and no digits.",
   "The rule is not never spend. It is spend on purpose, and let nothing creep in quietly.")
sc("CLOSE", "KDAY", "his face in close-up, calm and slightly amused, morning light.",
   "Lifestyle creep is not one big decision. It is a hundred small yeses that nobody remembers making.")
sc("SIT", "KDAY", "he sits at the kitchen table holding a mug, looking at the camera with a quiet smile, a small shield icon floating at the right.",
   "Your hundred small noes feel boring. But over ten years, boring turns out to be quietly powerful.")

# ---- acto 4: el giro / la prueba ----
sc("WIDE", "STREET", "an apartment building at dusk with a friend silhouette sitting on the front steps with his head in his hands, a stack of gray envelopes beside him.",
   "In year nine, one friend loses his job. His lease, rent, and credit card bills do not pause.")
sc("CLOSE", "LIVING", "a cropped friend silhouette with slumped shoulders at the doorway, Sam's kind face in the foreground, warm hallway light.",
   "He shows up at your door, embarrassed, and you invite him in for coffee without asking questions.")
sc("SIT", "LIVING", "he sits on the couch beside a friend silhouette, leaning slightly toward him with a patient, listening posture, two mugs on the table.",
   "You do not lend money you cannot spare, and you do not lecture. You listen first.")
sc("HAND", "KDAY", "two hands, one holding a pen, one pointing at a notebook page filled with small hand-drawn expense icons, no letters and no digits.",
   "You do help him write out every expense, just the way you once did.")
sc("MACRO", "DESK", "a notebook page with a long bar for rent, a medium bar for a car, a medium bar for travel, and a tall pile of tiny bars, no readable text and no digits.",
   "Together you see the pattern. Every raise had quietly become a bigger rent, a bigger payment, and a bigger weekend.")
sc("CLOSE", "LIVING", "a cropped friend silhouette looking up with a sad but relieved expression, Sam in the foreground listening, soft lamp light.",
   "He looks up and says, I thought I was being successful, but I have been running in place.")
sc("SIT", "LIVING", "he sits on the couch with a reassuring posture, one hand open, a small green sprout icon floating near his head.",
   "You tell him it is not too late. A new rule can start with any paycheck.")
sc("WIDE", "STREET", "a friend silhouette handing keys to a dealership attendant silhouette next to a sleek sports car, Sam small at the far edge of the frame.",
   "A few months later, he gives back the leased sports car and starts saving a little from every paycheck.")
sc("SIT", "KNIGHT", "he sits at the kitchen table at night alone with a mug, a faint empty chair beside him, a calm but honest expression.",
   "You admit something honest. Saying no cost you a few trips, and some friendships grew distant.")
sc("CLOSE", "KNIGHT", "his face in close-up, quietly thoughtful, a hint of regret in the eyes, lamp light.",
   "That is a real price, and it is worth thinking about before you copy anyone else.")
sc("HAND", "LIVING", "a hand holding the worn brown wallet, thumb resting on the frayed corner, soft light.",
   "The goal is not to win a race. The goal is to feel safe and spend on what you love.")
sc("WIDE", "LIVING", "a wide view of the living room with Sam and the three friend silhouettes gathered around the coffee table at night, warm lamplight.",
   "And so we come back to your living room, and the friends who finally ask how.")
sc("SIT", "LIVING", "he sits on the couch holding the worn brown wallet in both hands, a friendly open expression, looking at the camera.",
   "You pick up your worn wallet and tell them the simple truth, a little at a time.")
sc("CLOSE", "LIVING", "his face in close-up, warm and sincere, a faint glow on his cheek.",
   "You never earned more than them. You just refused to let each raise quietly rewrite your life.")
sc("STAND", "LIVING", "he stands by the couch as three friend silhouettes lean forward with curious faces, one with a hand raised in a question.",
   "They are quiet for a moment. Then one of them says, so where do I start?")

# ---- cierre ----
sc("SIT", "KDAY", "he sits at the kitchen table looking at the camera with a warm, calm expression, a mug and a notebook in front of him.",
   "So here is your point of view. A raise is a gift, and you decide who receives it.")
sc("MACRO", "DESK", "a notebook open with a flat horizontal line drawn across the page and a pen resting on it, no text and no digits.",
   "Step one, set a monthly spending line that fits your life today, and adjust it only for rising prices.")
sc("HAND", "KDAY", "a hand holding a smartphone, the screen shows a flat icon of an arrow moving from a wallet to a shield, no readable text and no digits.",
   "Step two, send most of every raise to saving or investing automatically, before it reaches your daily account.")
sc("MACRO", "DESK", "a small flat illustration of a gift box icon and a ticket icon beside a tiny jar on a dark wooden table, no text and no digits.",
   "Step three, keep a small fun fund, so you can enjoy life without guilt or drift.")
sc("STAND", "KDAY", "he stands in the kitchen in morning light leaning on the counter with a calm expression, a small shield icon floating over the window.",
   "If friends tease you, remember that spending to impress is a bill that never stops arriving.")
sc("SIT", "CLEAN", "He sits at a table looking at the camera with a friendly smile; floating at the right next to his head, a large flat icon of a red subscribe button with a bell, thick outline, no text.",
   "If this story made you think about your own raises, subscribe, and come back for the next quiet story.")
sc("MACRO", "DESK", "a closed notebook with a pen on top and a hand-drawn shield icon on the cover, on a dark wooden table, no letters and no digits.",
   "This video is for education only, not financial advice. Rates, expenses and risks differ for everyone, so speak with a licensed professional about your own situation.")
sc("WIDE", "STREET", "he walks home along a quiet sidewalk in the evening, small and relaxed, a long warm sunset behind him.",
   "You walk home in the evening, in the same sweatshirt, with the same wallet and a very different future.")
sc("MACRO", "DESK", "the worn brown leather wallet with the frayed corner on a dark wooden table beside a single coffee mug, soft morning light, no letters and no digits.",
   "The wallet is old. Your options are new.")

if __name__ == "__main__":
    emit(S, "v5", "Video 5: POV: You Said No to Lifestyle Creep - And Your Friends Noticed")
