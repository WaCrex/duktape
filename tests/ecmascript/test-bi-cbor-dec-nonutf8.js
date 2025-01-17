/*
 *  Test for current behavior when decoding non-UTF-8 CBOR text strings
 *  (technically invalid CBOR).
 */

/*===
"foo"
"foo\ud800"
"foo\ud800bar"
"\ufffd\ufffd"
TypeError
"\U0001f4a9"
===*/

function test(hexInput) {
    try {
        print(Duktape.enc('jx', CBOR.decode(Duktape.dec('hex', hexInput))));
    } catch (e) {
        print(e.name);
    }
}

// Valid CBOR text string.
test('63666f6f');

// CESU-8 string, invalid UTF-8 and thus invalid CBOR: unpaired U+D800 in string.
//
// Current behavior: decode into an ECMAScript string as is.
// Could also reject, or use U+FFFD.
test('66666f6feda080');
test('69666f6feda080626172');

// Invalid UTF-8 and CESU-8.
//
// Current behavior: decode as is, except if would map into a Duktape
// Symbol which is rejected.
test('62c080');  // "long form" U+0000 => two replacements
test('6482112233');  // would map to Symbol => TypeError

// Input has valid surrogate pair (CESU-8), which is still invalid
// UTF-8.
//
// Current behavior: accepted as is.  The surrogate pair then gets
// combined into a single codepoint in WTF-8 intern check.
/*
>>> u'\ud83d'.encode('utf-8')
'\xed\xa0\xbd'
>>> u'\udca9'.encode('utf-8')
'\xed\xb2\xa9'
*/
test('66eda0bdedb2a9');
