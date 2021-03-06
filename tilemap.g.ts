// Auto-generated code. Do not edit.
namespace myTiles {
    //% fixedInstance jres blockIdentity=images._tile
    export const transparency16 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile1 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile2 = image.ofBuffer(hex``);
    //% fixedInstance jres blockIdentity=images._tile
    export const tile3 = image.ofBuffer(hex``);

    helpers.registerTilemapFactory(function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "level": return tiles.createTilemap(hex`1600100001010101010101010101010101010101000000000000010101010101010101010101010101010000000000000101010101010101010101010101010100000000000001010101010101010101010101010101000000000000010101010101010101010101010101010000000000000101010101010101010101030101010100000000000003030303030101010101010101010303000000000000010101010101010103030101010101010000000000000101010101010303030101010101010100000000000001010101010101010101010101010101000000000000010101010101010101010101010101010000000000000101010101010101010101010101010100000000000001010101010101010101010101010101000000000000010101010101010101010101010101010000000000000202020202020202020202020202020200000000000002020202020202020202020202020202000000000000`, img`
......................
......................
......................
......................
......................
......................
......................
......................
......................
......................
......................
......................
......................
......................
......................
......................
`, [myTiles.transparency16,myTiles.tile1,myTiles.tile2,myTiles.tile3], TileScale.Sixteen)
        }
        return null;
    })

}
// Auto-generated code. Do not edit.
