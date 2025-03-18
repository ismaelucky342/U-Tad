package ex00;

public interface Strategy {
	public void format(String text);
}

public class EchoTextFormatter implements Strategy {
    @Override
    public void format(String text) {
        System.out.println("[EchoTextFormatter]:" + text);
    }
}

public class CamelTextFormatter implements Strategy {
	@Override
	public void format(String text) {
		StringBuilder cmaelText = new StringBuilder("");
		for (int i = 0; i < text.length(); i++) {
			if (i % 2 == 0) {
				cmaelText.append(Character.toUpperCase(text.charAt(i)));
			} else {
				cmaelText.append(Character.toLowerCase(text.charAt(i)));
			}
		}
		System.out.println("[CamelTextFormatter]:" + cmaelText.toString());
	}
}

