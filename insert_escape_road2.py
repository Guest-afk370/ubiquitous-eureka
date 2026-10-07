from pathlib import Path

path = Path('Index.html')
text = path.read_text(encoding='utf-8')
needle = '        <a href="Fleeing the Complex.html">Play Now</a>\n      </article>\n      <article class="card">\n'
insert = (
    '        <a href="Fleeing the Complex.html">Play Now</a>\n'
    '      </article>\n'
    '      <article class="card">\n'
    '        <img class="card__art" src="https://via.placeholder.com/320x180.png?text=Escape+Road+2" alt="Escape Road 2 box art">\n'
    '        <h2>Escape Road 2</h2>\n'
    '        <p>A high-speed escape game where you dodge traffic, jump ramps, and race through hectic lanes to survive and reach the finish.</p>\n'
    '        <a href="escape-road-2.html">Play Now</a>\n'
    '      </article>\n'
    '      <article class="card">\n'
)
if needle not in text:
    raise SystemExit('Needle not found')
text = text.replace(needle, insert, 1)
path.write_text(text, encoding='utf-8')
print('Inserted Escape Road 2 card.')
