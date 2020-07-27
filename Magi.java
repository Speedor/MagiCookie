package xxxxxxxx;

/**
 * @author Speedor
 * @program spider
 * @description Magi 搜索引擎搜索 cookie 生成
 * @create 2020-07-25 20:42
 **/
public class Magi {

    private static String hexJoin(String arg) {
        int[] v0x4b082b = {0xf, 0x23, 0x1d, 0x18, 0x21, 0x10, 0x1, 0x26, 0xa, 0x9, 0x13, 0x1f, 0x28, 0x1b, 0x16, 0x17, 0x19, 0xd,
                0x6, 0xb, 0x27, 0x12, 0x14, 0x8, 0xe, 0x15, 0x20, 0x1a, 0x2, 0x1e, 0x7, 0x4, 0x11, 0x5, 0x3, 0x1c,
                0x22, 0x25, 0xc, 0x24};
        String[] v0x4da0dc = new String[40];
        for (int v0x20a7bf = 0; v0x20a7bf < arg.length(); v0x20a7bf++) {
            char v0x385ee3 = arg.charAt(v0x20a7bf);
            for (int v0x217721 = 0; v0x217721 < v0x4b082b.length; v0x217721++) {
                if (v0x4b082b[v0x217721] == v0x20a7bf + 0x1) {
                    v0x4da0dc[v0x217721] = String.valueOf(v0x385ee3);
                }
            }
        }
        return String.join("", v0x4da0dc);
    }


    private static String hexXor(String v0x4e08d8, String v0x23a392) {
        StringBuilder v0x5a5d3b = new StringBuilder();
        for (int v0xe89588 = 0x0; v0xe89588 < v0x4e08d8.length() && v0xe89588 < v0x23a392.length(); v0xe89588 += 0x2) {
            int v0x105f59 = Integer.parseInt(v0x23a392.substring(v0xe89588, v0xe89588 + 0x2), 16);
            int v0x401af1 = Integer.parseInt(v0x4e08d8.substring(v0xe89588, v0xe89588 + 0x2), 16);
            String v0x189e2c = Integer.toHexString(v0x401af1 ^ v0x105f59);
            if (v0x189e2c.length() == 0x1) {
                v0x189e2c = "0" + v0x189e2c;
            }
            v0x5a5d3b.append(v0x189e2c);
        }
        return v0x5a5d3b.toString();
    }

    /**
     *   测试：
    *         arg1 = "E609CBF569B6DB613EDB0C3E3174149363F521A9"
    *         acw_sc__v2 = "5f1e7681965cf7c53baeafe680320df91b843110"
     * @param args
     */
    public static void main(String[] args) {
        String key = "3000176000856006061501533003690027800375";
        String v0x23a392 = hexJoin("E609CBF569B6DB613EDB0C3E3174149363F521A9");
        String arg2 = "acw_sc__v2=" + hexXor(key, v0x23a392);
        System.out.println(arg2);
    }
}
