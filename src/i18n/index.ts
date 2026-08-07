import es from "./es.json";
import en from "./en.json";
import fr from "./fr.json";

export const defaultLang = "es" as const;

/** Códigos BCP-47 completos, para el atributo `lang` y `og:locale`. */
export const localeTags = {
	es: "es-MX",
	en: "en",
	fr: "fr",
} as const;

export const dictionaries = { es, en, fr };

export type Lang = keyof typeof dictionaries;
/** `es.json` es la fuente de verdad: si una clave falta en otro idioma, TypeScript lo marca. */
export type TranslationKey = keyof typeof es;

export const languages = Object.keys(dictionaries) as Lang[];

export function isLang(value: string | undefined): value is Lang {
	return value !== undefined && (languages as string[]).includes(value);
}

/**
 * Deduce el idioma del primer segmento de la ruta.
 * `/` → es (defaultLocale sin prefijo) · `/en/...` → en · `/fr/...` → fr
 */
export function getLangFromUrl(url: URL): Lang {
	const [, segment] = url.pathname.split("/");
	return isLang(segment) ? segment : defaultLang;
}

/** Devuelve el traductor del idioma dado. Lanza en build si la clave no existe. */
export function useTranslations(lang: Lang) {
	const dict = dictionaries[lang];
	return function t<K extends TranslationKey>(key: K): (typeof es)[K] {
		return dict[key] as (typeof es)[K];
	};
}

/**
 * Prefija una ruta interna con el idioma. El idioma por defecto no lleva prefijo.
 * Siempre devuelve barra final, para que coincida con el `canonical` que genera
 * Astro en build estático (`/en/index.html` → `/en/`).
 */
export function localizePath(path: string, lang: Lang): string {
	const clean = `/${path.replace(/^\/|\/$/g, "")}`;
	const prefixed = lang === defaultLang ? clean : `/${lang}${clean === "/" ? "" : clean}`;
	return prefixed.endsWith("/") ? prefixed : `${prefixed}/`;
}
